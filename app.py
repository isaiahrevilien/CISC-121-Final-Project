import gradio as gr
import random
import time

class ShuttleStop:
    def __init__(self, name, crowd_count):
        self.name = name
        self.crowd_count = crowd_count
    
    def __repr__(self):
        return f"{self.name}: {self.crowd_count}"

def generate_shuttle_stops():
    """Generate random shuttle stop data using REAL Queen's University campus locations"""
    # Queen's University campus stops
    stop_names = [
        "Goodes Hall",
        "Chernoff Hall",
        "Grant Hall",
        "Stuart Street",
        "Victoria Hall",
        "Bader Lane",
        "Ellis Hall",
        "Waldron Tower",         # My residence!
        "Jean Royce Hall",
        "Convocation Hall",      # Class for CISC 121
        "Queen's West Campus",
        "Union Street",
        "Kingston Hall",
        "Botterell Hall",        # Wally's!
        "Mackintosh-Corry Hall",
        "Stauffer Library"
    ]
    
    # Use 8 random unique stops
    selected_stops = random.sample(stop_names, 8)
    stops = []
    for name in selected_stops:
        crowd = random.randint(10, 100)
        stops.append(ShuttleStop(name, crowd))
    
    return stops

def format_list(stops):
    """Format the list for display"""
    return ", ".join([f"{stop.name}({stop.crowd_count})" for stop in stops])

def render_bars(stops, highlight_indices, action):
    """Render bars representing crowd counts"""
    if not stops:
        return '<div style="text-align:center;">No data to display</div>'
    
    html = '<div style="display:flex; justify-content:center; gap:8px; align-items:flex-end; flex-wrap:wrap;">'
    max_val = max([stop.crowd_count for stop in stops]) if stops else 1
    
    for i, stop in enumerate(stops):
        color = "#3498db"  # normal blue color
        if i in highlight_indices:
            color = "#e74c3c" if action == "merge" else "#f1c40f"  # red for merging, yellow for comparing
        
        height = int((stop.crowd_count / max_val) * 150)
        html += f'''
        <div style="text-align:center; width:70px;">
            <div style="height:{height}px; background-color:{color}; width:100%; border-radius:5px 5px 0 0; transition:all 0.3s;"></div>
            <div style="background-color:#2c3e50; color:white; padding:5px; font-size:11px; border-radius:0 0 5px 5px;">
                <strong>{stop.name}</strong><br>
                {stop.crowd_count}
            </div>
        </div>
        '''
    html += '</div>'
    return html

def merge_sort_steps(stops):
    """Merge sort that yields each step for visualization"""
    if len(stops) <= 1:
        yield stops, [i for i in range(len(stops))], "base"
        return
    
    mid = len(stops) // 2
    left = stops[:mid]
    right = stops[mid:]
    
    # Recursively sort left and right
    left_result = None
    right_result = None
    
    for left_sorted, highlights, action in merge_sort_steps(left):
        left_result = left_sorted
        yield left_sorted, highlights, action
    
    for right_sorted, highlights, action in merge_sort_steps(right):
        right_result = right_sorted
        yield right_sorted, highlights, action
    
    # Merge the sorted halves
    merged = []
    i = j = 0
    
    yield stops, [mid-1, mid], "split"
    
    while i < len(left_result) and j < len(right_result):
        if left_result[i].crowd_count <= right_result[j].crowd_count:
            merged.append(left_result[i])
            yield merged, [len(merged)-1], "compare"
            i += 1
        else:
            merged.append(right_result[j])
            yield merged, [len(merged)-1], "compare"
            j += 1
    
    while i < len(left_result):
        merged.append(left_result[i])
        yield merged, [len(merged)-1], "merge"
        i += 1
    
    while j < len(right_result):
        merged.append(right_result[j])
        yield merged, [len(merged)-1], "merge"
        j += 1
    
    yield merged, [i for i in range(len(merged))], "complete"

def visualize_merge_sort(numbers):
    """Main visualization function"""
    # Parse the input
    try:
        nums = [int(x.strip()) for x in numbers.split(",")]
        if not nums:
            yield "Error: Please enter at least one number"
            return
    except:
        yield "Error: Please enter whole numbers separated by commas (e.g., 5,3,2,4,1)"
        return
    
    # Create shuttle stops from numbers
    stops = [ShuttleStop(f"Stop {i+1}", val) for i, val in enumerate(nums)]
    
    # Run merge sort and yield frames
    for sorted_stops, highlights, action in merge_sort_steps(stops):
        frame = render_bars(sorted_stops, highlights, action)
        yield frame
        time.sleep(0.5)
    
    # Final frame
    yield render_bars(sorted_stops, [], "done")

def generate_random_numbers():
    """Generate random numbers for demo"""
    random_nums = [random.randint(10, 100) for _ in range(6)]
    return ",".join(map(str, random_nums))

# Gradio UI
with gr.Blocks(theme='shivi/calm_seafoam') as demo:
    gr.Markdown("<center><h1>🔄 Merge Sort Visualizer | Queen's Shuttle Edition</h1></center>")
    gr.Markdown("<center><i>Ranking campus stops by crowd count using Divide & Conquer</i></center>")
    gr.Markdown("---")
    
    with gr.Row():
        with gr.Column():
            input_numbers = gr.Textbox(
                label="👥 Enter crowd counts (numbers separated by commas)", 
                placeholder="e.g., 12, 6, 7, 3, 20, 15",
                lines=2
            )
            with gr.Row():
                random_btn = gr.Button("🎲 Random Numbers", variant="secondary")
                run_button = gr.Button("🚌 Run Merge Sort", variant="primary")
        
        with gr.Column():
            output_html = gr.HTML(label="Merge Sort Animation")
    
    gr.Markdown("---")
    gr.Markdown("""
    ### 📍 Queen's Campus Locations Featured:
    **Goodes Hall** , **Chernoff Hall** , **Grant Hall** , **Victoria Hall** , **Bader Lane**  
    **Ellis Hall** , **Waldron Tower (My residence! 😊)** , **Convocation Hall (CISC 121 Lecture)** , **Stauffer Library** , **Mackintosh-Corry Hall**
    """)
    
    random_btn.click(generate_random_numbers, outputs=input_numbers)
    run_button.click(visualize_merge_sort, inputs=input_numbers, outputs=output_html)

demo.launch()
