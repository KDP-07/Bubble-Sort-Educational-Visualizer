# Bubble Sort Educational Visualizer
## Author: Kyan Perera

### Why I Chose Bubble Sort
I’m choosing bubble sort because its one of the simplest sorting algorithms, and I find the step-by-step nature of the algorithm easy to visualize. The algorithm repeatedly compares side-by-side elements, making it ideal for an educational demonstration app.

### Computational Thinking
Decomposition:
1. Start at beginning of list
2. Compare adjacent elements
3. Swap them if in wrong order
4. Move to next pair
5. After each full pass, largest remaining value “bubbles” to the end
6. Repeat until list is sorted
7. Track every comparison and swap for visualization purposes

Pattern Recognition:  
Bubble Sort repeatedly uses the same pattern 
- Compare 2 neighbouring values   
- Swap if needed  
- Amount of unsorted elements goes down with each pass  

Abstraction:  
Shown to the user   
- Every comparison  
- Every swap  
- The list after each change  
- The final sorted list  

Hidden from the user   
- Any data conversion (string to int, etc.)  
- Loop counters/index movement  
- Error handling logic (users should see human-readable error messages, not technical diagnostics)    

Algorithmic Design:  

Input - list of integers

Processing - convert input string to Python list, apply bubble sort, record every comparison, swap, intermediate list state

Output - Step by step text explanation showing how the list changes

Flowchart:

[./Bubble Sort Visualization-2025-12-10-044254.png
](https://huggingface.co/spaces/KDP07/Kyan_CISC102_Final_Project/resolve/main/Bubble%20Sort%20Visualization-2025-12-10-044254.png)

### Steps to Run

Enter your numbers - Type a list of integers separated by commas in the text box (for example: 5, 3, 8, 1)

Click the "Sort" button - This initializes the visualization and shows your numbers in their starting positions

Click "Next Step" repeatedly - Each click advances the algorithm forward, showing you which two numbers are being compared (highlighted in pink with red borders), and the current state of the array after any swaps

Watch the sorting process - As you click through the steps, you'll see how Bubble Sort compares adjacent pairs and swaps them when needed to gradually move larger numbers toward the end

Reach the sorted result - The "Next Step" button will disable automatically when the array is fully sorted

### Hugging face Link

https://huggingface.co/spaces/KDP07/Kyan_CISC102_Final_Project

### Testing & Verification

As shown in the video below, I tested for a normal input, an already sorted input, a reverse sorted input, an input with duplicates, an input with negatives, a single integer input, an incorrect input that uses letters, and an incorrect empty input.
https://huggingface.co/spaces/KDP07/Kyan_CISC102_Final_Project/resolve/main/Screen%20Recording%202025-12-09%20at%2011.18.25%E2%80%AFPM.mov

### Acknowledgement 

Thank you to my professor, Mr. Kain, for your guidance and support throughout this course. This project makes use of Gradio for the interface, Hugging Face, and Python standard libraries. During this project, I used ChatGPT level 4 AI to help build the UI portion of my code, as shown in the code.

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
