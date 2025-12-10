import gradio as gr

# -----------------------------
# INPUT PARSING & VALIDATION
# -----------------------------
def parse_input(number_string: str):
    """
    Converts an inputted comma-separated string into a list of integers.
    Includes detailed error handling so the program never crashes from bad input.
    """
    if number_string is None:
        raise ValueError("No input provided.")

    stripped = number_string.strip()
    if stripped == "":
        raise ValueError("Input is empty. Enter a comma-separated list of integers.")

    # Split by commas and strip whitespace around each element
    parts = [p.strip() for p in stripped.split(",")]
    nums = []

    for p in parts:
        # Detect cases like "1,,2" or "1, " (faulty input)
        if p == "":
            raise ValueError("Empty value detected. Make sure numbers are separated by commas.")

        try:
            nums.append(int(p))   # Convert each token to int
        except ValueError:
            # Provide a helpful, specific error message
            raise ValueError(f"Invalid number: '{p}'. Enter only integers.")

    return nums


# -----------------------------
# BUBBLE SORT IMPLEMENTATION
# -----------------------------
def bubble_sort_steps(arr):
    """
    Runs Bubble Sort on a copy of the list and records EVERY key step:
    - Each comparison
    - Each swap
    - Each pass number
    - Early stopping if no swaps were made
    """

    steps = []          # Stores lines of text describing each action
    a = arr.copy()      # Work on a copy so we don't modify user input
    n = len(a)

    # If the list has 0 or 1 items, no sorting needed
    if n <= 1:
        steps.append(f"No comparisons needed — list has only {n} element(s).")
        steps.append(f"Final sorted list: {a}")
        return steps

    # Outer loop controls how many passes we make
    for i in range(n):
        swapped_this_pass = False

        # Label the pass for clarity in the output
        steps.append(f"\n--- Pass {i+1} (checking indices 0 to {n-i-2}) ---")

        # Inner loop compares adjacent pairs
        for j in range(0, n - i - 1):
            steps.append(f"Comparing a[{j}]={a[j]} and a[{j+1}]={a[j+1]}")

            # Swap logic
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]   # Swap elements
                swapped_this_pass = True
                steps.append(f"Swapped → {a}")
            else:
                steps.append(f"No swap → {a}")

        # Optimization: If no swaps were made, the list is already sorted
        if not swapped_this_pass:
            steps.append(f"No swaps in Pass {i+1} — list is already sorted early.")
            break

    # Final line of output
    steps.append(f"\nFinal sorted list: {a}")
    return steps


# -----------------------------
# GRADIO CALLBACK FUNCTION
# -----------------------------
def run_bubble_sort(user_input: str):
    """
    Called when the user presses the Gradio button.
    1. Parses user input safely.
    2. Runs Bubble Sort.
    3. Displays the step-by-step output or an error message.
    """
    try:
        arr = parse_input(user_input)
    except ValueError as e:
        return "Input error: " + str(e)

    # Convert list of steps to one long readable string
    result = "\n".join(bubble_sort_steps(arr))
    return result


# ============================================================
#  HTML User Interface (made with Level 4 AI)
# ============================================================

def bubble_sort_passes(arr):
    """Compute ONLY end-of-pass states for next-step UI."""
    a = arr.copy()
    n = len(a)
    passes = []

    if n <= 1:
        passes.append({'state': a.copy(), 'pointer': 0, 'comparing': []})
        return passes

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # Capture state during comparison
            passes.append({'state': a.copy(), 'pointer': n - i - 1, 'comparing': [j, j+1]})
            
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        bubbled_index = n - i - 1
        passes.append({'state': a.copy(), 'pointer': bubbled_index, 'comparing': []})

        if not swapped:
            break

    return passes


def render_array_html(state, comparing_indices):
    """Return simple HTML boxes with highlighted elements being compared."""
    box_css = (
        "display:inline-block;padding:10px 14px;margin:5px;border:1px solid #cbd5e1;"
        "border-radius:6px;background:#ffffff;font-family:monospace;font-size:18px;color:#000000;"
    )
    
    highlight_css = (
        "display:inline-block;padding:10px 14px;margin:5px;border:2px solid #ef4444;"
        "border-radius:6px;background:#fee2e2;font-family:monospace;font-size:18px;color:#000000;"
    )

    boxes = ""
    for i, v in enumerate(state):
        if i in comparing_indices:
            boxes += f'<div style="{highlight_css}">{v}</div>'
        else:
            boxes += f'<div style="{box_css}">{v}</div>'

    return f"""
    <div style="padding:10px;background:#f1f5f9;border-radius:8px;border:1px solid #e2e8f0;">
        {boxes}
    </div>
    """


def init_visual(user_input: str):
    """Initialize visualization and return pass 0."""
    try:
        arr = parse_input(user_input)
    except ValueError as e:
        # Return error message, empty states, disable next button
        return (
            f"<b>Error:</b> {e}",  # HTML output
            [],                     # passes_state
            0,                      # index_state
            gr.update(interactive=False)  # FIXED: Changed from gr.Button.update
        )

    passes = bubble_sort_passes(arr)
    first = passes[0]

    # Enable Next button only if more than 1 pass exists
    disable_next = len(passes) <= 1

    return (
        render_array_html(first["state"], first["comparing"]),
        passes,
        0,
        gr.update(interactive=not disable_next)  # FIXED: Changed from gr.Button.update
    )



def next_step(passes, idx):
    """Advance one pass at a time."""
    if not passes:
        return ("<b>Error:</b> Initialize first.", 0, gr.update(interactive=False))

    new_idx = idx + 1
    if new_idx >= len(passes):
        # Already finished
        last = passes[-1]
        return (
            render_array_html(last["state"], last["comparing"]),
            idx,
            gr.update(interactive=False)  # FIXED: Changed from disabled=True
        )

    entry = passes[new_idx]
    disable = (new_idx == len(passes) - 1)

    return (
        render_array_html(entry["state"], entry["comparing"]),
        new_idx,
        gr.update(interactive=not disable)  # FIXED: Changed from disabled=disable
    )


# ---------------------------------------
# HTML + Gradio UI (Made with Level 4 AI)
# ---------------------------------------
with gr.Blocks() as demo:

    gr.Markdown("# Educational Bubble Sort Visualizer")
    gr.Markdown(
        "Enter numbers, click **Sort**, then press **Next Step** "
        "to move forward one sorting pass at a time."
    )

    inp = gr.Textbox(label="Enter numbers:", placeholder="Example: 5, 3, 8, 1")
    init_btn = gr.Button("Sort")
    next_btn = gr.Button("Next Step", interactive=False)  # FIXED: Added interactive parameter

    html_out = gr.HTML("<i>Visualization appears here.</i>")

    passes_state = gr.State([])
    index_state = gr.State(0)

    init_btn.click(
        init_visual,
        inputs=[inp],
        outputs=[html_out, passes_state, index_state, next_btn]
    )

    next_btn.click(
        next_step,
        inputs=[passes_state, index_state],
        outputs=[html_out, index_state, next_btn]
    )

if __name__ == "__main__":
    demo.launch()
