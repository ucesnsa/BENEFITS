import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np

# Create figure with landscape orientation
fig, ax = plt.subplots(figsize=(18, 10))
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.axis('off')

# Define colors (softer, more professional)
color_input = '#E3F2FD'  # Light blue
color_process = '#FFF3E0'  # Light orange
color_rules = '#E8F5E9'  # Light green
color_output = '#F3E5F5'  # Light purple
color_arrow = '#424242'  # Dark gray


# Helper function to create rounded boxes
def create_box(x, y, width, height, text, color, fontsize=10, fontweight='normal', alpha=1.0):
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.15",
                         edgecolor='#333333',
                         facecolor=color,
                         linewidth=2.5,
                         alpha=alpha)
    ax.add_patch(box)

    # Split text for better formatting
    lines = text.split('\n')
    num_lines = len(lines)
    y_text = y + height / 2 + (num_lines - 1) * 0.15

    for i, line in enumerate(lines):
        ax.text(x + width / 2, y_text - i * 0.3, line,
                ha='center', va='center',
                fontsize=fontsize, fontweight=fontweight)


# Helper function to create arrows
def create_arrow(x1, y1, x2, y2, style='->', width=3):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle=style,
                            color=color_arrow,
                            linewidth=width,
                            zorder=1)
    ax.add_patch(arrow)


# Title
ax.text(9, 9.3, 'BENEFITS Employment Microsimulation Model',
        ha='center', va='center', fontsize=20, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', linewidth=2))

# ===== ROW 1: INPUT & PREPARATION =====

# STEP 1: Survey Data
create_box(0.5, 6.5, 2.8, 1.8,
           'STEP 1\nSurvey Data\n\nPopulation with\nindividual attributes',
           color_input, fontsize=11, fontweight='bold')

create_arrow(3.3, 7.4, 4.2, 7.4)

# STEP 2: Data Cleaning
create_box(4.2, 6.5, 2.8, 1.8,
           'STEP 2\nData Cleaning\n\n• Standardize categories\n• Create age groups\n• Handle missing data',
           color_process, fontsize=10, fontweight='bold')

create_arrow(7, 7.4, 7.8, 7.4)

# STEP 3: Baseline Population
create_box(7.8, 6.5, 3.2, 1.8,
           'STEP 3\nBaseline Population (T=0)\n\nAge | Employment | Disability\nGender | Ethnicity',
           color_input, fontsize=10, fontweight='bold')

create_arrow(9.4, 6.5, 9.4, 5.5)

# ===== ROW 2: CORE MODEL =====

# STEP 4: Transition Rules (LARGE CENTER BOX)
create_box(7.2, 2.8, 4.4, 2.5,
           'STEP 4: Transition Rules Engine\n\nFor each individual, calculate probability of next employment state:\n\n',
           color_rules, fontsize=11, fontweight='bold')

# Add rule details
rules = [
    '• INERTIA: 70% probability to stay in current state',
    '• AGE: Young adults → Student/Part-time | Seniors → Retired',
    '• DISABILITY: Limited ability → Reduced full-time probability',
    '• GENDER & ETHNICITY: Adjust probabilities based on patterns'
]

y_rule = 4.3
for i, rule in enumerate(rules):
    ax.text(9.4, y_rule - i * 0.35, rule, fontsize=9, ha='center')

ax.text(9.4, 3.1, '↓ Apply random selection based on probabilities ↓',
        fontsize=9, ha='center', style='italic')

create_arrow(9.4, 2.8, 9.4, 2.0)

# STEP 5: Simulation Loop
create_box(7.2, 0.5, 4.4, 1.3,
           'STEP 5: Time Simulation\n\nT=1 → T=2 → T=3 → ... → T=n\nUpdate states each period',
           color_process, fontsize=10, fontweight='bold')

# Loop arrow
create_arrow(11.8, 1.2, 12.5, 3.5, style='->', width=2.5)
create_arrow(12.5, 3.5, 12.5, 5.0, style='->', width=2.5)

ax.text(13, 4, 'Loop', fontsize=9, rotation=90, ha='center', fontweight='bold')

# ===== ROW 3: OUTPUTS =====

# Output boxes on the right
outputs_x = 13.5
output_width = 3.5
output_height = 1.2

create_box(outputs_x, 6.8, output_width, output_height,
           'OUTPUT 1\nTransition Matrix\n\nWho moves from state A to state B?',
           color_output, fontsize=10, fontweight='bold')

create_box(outputs_x, 5.2, output_width, output_height,
           'OUTPUT 2\nEmployment Composition\n\nBefore vs After shares',
           color_output, fontsize=10, fontweight='bold')

create_box(outputs_x, 3.6, output_width, output_height,
           'OUTPUT 3\nEquity Analysis\n\nOutcomes by vulnerability groups',
           color_output, fontsize=10, fontweight='bold')

# Arrows from simulation to outputs
create_arrow(11.6, 1.2, 13, 6.8)
create_arrow(11.6, 1.2, 13, 5.8)
create_arrow(11.6, 1.2, 13, 4.2)

# ===== POLICY INSIGHT BOX =====
insight_box = FancyBboxPatch((1, 0.1), 10, 0.6,
                             boxstyle="round,pad=0.1",
                             edgecolor='#FF6B35',
                             facecolor='#FFF9E6',
                             linewidth=2.5)
ax.add_patch(insight_box)

ax.text(6, 0.4,
        'Policy Insight: Compare outcomes by age, disability, gender, ethnicity → Identify inequalities → Design interventions',
        ha='center', va='center', fontsize=11, style='italic', fontweight='bold')

# ===== LEGEND =====
legend_patches = [
    mpatches.Patch(color=color_input, label='Input Data', edgecolor='black', linewidth=1.5),
    mpatches.Patch(color=color_process, label='Processing Steps', edgecolor='black', linewidth=1.5),
    mpatches.Patch(color=color_rules, label='Model Rules/Logic', edgecolor='black', linewidth=1.5),
    mpatches.Patch(color=color_output, label='Analysis Outputs', edgecolor='black', linewidth=1.5)
]

legend = ax.legend(handles=legend_patches, loc='upper left',
                   fontsize=9, frameon=True, fancybox=True,
                   edgecolor='black', framealpha=1)

plt.tight_layout()

# Save
from pathlib import Path
from datetime import datetime

script_dir = Path(__file__).parent
project_root = script_dir.parent.parent
output_folder = project_root / "0_Project_Overview" / "outputs" / "figures"
output_folder.mkdir(parents=True, exist_ok=True)

filename = f'microsimulation_model_diagram_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
save_path = output_folder / filename

plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"✅ Diagram saved to: {save_path}")

plt.show()