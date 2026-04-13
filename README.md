# 🔄 Merge Sort Visualizer | Queen's Shuttle Edition (Problem: Shuttle Stop Crowd Ranking)
Campus shuttle dispatchers need to quickly identify which stops have the highest crowding to send extra shuttles during peak hours. This program takes a list of shuttle stops with crowd estimates and ranks them by crowd count using Merge Sort, displaying a step-by-step visualization of how the ordering changes over time.

## Algorithm Name: Merge Sort
I chose Merge Sort because it provides a clear and structured way to visualize sorting through its divide-and-conquer approach. Unlike simpler algorithms, Merge Sort breaks the data into smaller pieces and then rebuilds it step-by-step in sorted order. This makes it especially useful for visual simulation, as users can see how smaller groups are merged together to form the final ranked list. The merging process is predictable and systematic, which makes it easier to animate and understand. Overall, Merge Sort is efficient and visually demonstrates how complex problems can be solved by breaking them into smaller parts.

## Problem Breakdown & Computational Thinking
### Decomposition
- Break the problem into generating shuttle stop data, performing merge sort, and displaying each step visually
- Separate the sorting process into splitting lists and merging them back together in order
- Divide the interface into components: data generation button, visualization area, and sorting controls

### Pattern Recognition
- The algorithm repeatedly splits the list into smaller halves until only single elements remain
- These smaller lists are then merged back together in sorted order by comparing values
- The merging process follows a consistent pattern of comparing the smallest elements from each sublist

### Abstraction
- Focus on key actions: splitting lists, comparing values, and merging sorted lists
- Hide low-level details such as recursion calls and index tracking
- Present shuttle stops and crowd counts visually instead of showing raw code or data structures

### Algorithm Design
- **Input** → generated list of shuttle stops with crowd counts
- **Processing** → merge sort algorithm runs step-by-step, recording each merge stage
- **Output** → visual updates show how the list is reorganized during each merge
- The GUI controls when sorting starts using a button and displays the evolving list states
- The goal is to create a visual “animation” showing how smaller groups are merged into a fully sorted list
- This helps demonstrate how shuttle stops are ranked from least to most crowded

### Flowchart
<img width="1594" height="2063" alt="Final Flowchart" src="https://github.com/user-attachments/assets/e0b15367-2428-4578-aa85-b33f68427235" />

## Demo video/gif/screenshot of test
https://github.com/user-attachments/assets/99980874-e5c4-42ae-be23-5f9747e7ba4c

## Steps to Run
1. Clone the repository and navigate to the project folder
2. Install dependencies: 'pip install -r requirements.txt'
3. Click **"Generate Shuttle Stops"** to create a dataset
4. Click **"Run Merge Sort"**
5. Watch the step-by-step merge sort visualization
6. View the final ranked list of shuttle stops

## Hugging Face Link
https://huggingface.co/spaces/isaiahrev/CISC-121-Final-Project

## Author & Acknowledgment
Author: Isaiah Révilien

Acknowledgements: Used the Hugging Face documentation ([https://huggingface.co/docs](https://huggingface.co/docs)) to deploy the app. Additionally, used the Gradio quickstart guide ([https://www.gradio.app/guides/quickstart](https://www.gradio.app/guides/quickstart)) to implement the user interface. AI Disclosure: Level 2 AI assistance (GitHub Copilot) was used to help refine code syntax and debug minor issues. All core logic, algorithm implementation, and design decisions were completed independently.
