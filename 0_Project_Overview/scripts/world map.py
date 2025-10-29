import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib.patches as mpatches
from pyproj import CRS
import os
from datetime import datetime
from pathlib import Path

# Load world map data and filter for Europe
try:
    # Load world data
    world = gpd.read_file("https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries_lakes.zip")

    # Define European countries to include in the map
    european_countries = [
        'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Czechia', 'Denmark',
        'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy',
        'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal',
        'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'United Kingdom', 'Norway',
        'Switzerland', 'Iceland', 'Albania', 'Serbia', 'Montenegro', 'Bosnia and Herzegovina',
        'North Macedonia', 'Kosovo', 'Moldova', 'Belarus', 'Ukraine', 'Turkey'
    ]

    # Find the correct column name
    name_col = None
    for col in ['NAME', 'NAME_EN', 'ADMIN', 'name']:
        if col in world.columns:
            name_col = col
            print(f"Using column: {col}")
            break

    # Filter for European countries
    europe = world[world[name_col].isin(european_countries)].copy()

    # Set proper CRS for Europe (ETRS89 Lambert Azimuthal Equal Area - EPSG:3035)
    # This is the official EU projection for statistical mapping
    europe = europe.to_crs('EPSG:3035')

except Exception as e:
    print(f"Error loading map data: {e}")
    exit()

# Define the countries to highlight with colors
participant_countries = {
    "Greece": "#FF6B6B",  # Coral red
    "Austria": "#4ECDC4",  # Turquoise
    "United Kingdom": "#45B7D1",  # Sky blue
    "Spain": "#FFA07A",  # Light salmon
    "Belgium": "#98D8C8",  # Mint green
    "Italy": "#95E77E",  # Light green
    "Sweden": "#FFD93D"  # Golden yellow
}

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 14))

# Plot all European countries with white fill and black borders
europe.plot(ax=ax, color='white', edgecolor='black', linewidth=0.5)

# Color the participant countries
for country, color in participant_countries.items():
    if name_col:
        # Handle different possible names for UK
        if country == "United Kingdom":
            # Try multiple variations
            uk_mask = (europe[name_col] == 'United Kingdom') | \
                      (europe[name_col] == 'UK') | \
                      (europe[name_col] == 'Britain') | \
                      (europe[name_col] == 'U.K.')
            if uk_mask.any():
                europe[uk_mask].plot(ax=ax, color=color, edgecolor='black', linewidth=0.8)
        else:
            country_mask = europe[name_col] == country
            if country_mask.any():
                europe[country_mask].plot(ax=ax, color=color, edgecolor='black', linewidth=0.8)
            else:
                print(f"Country not found: {country}")

# Remove axis ticks and labels
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Add title
plt.title('European Participant Countries', fontsize=20, fontweight='bold', pad=20)

# Create legend
legend_elements = []
for country, color in participant_countries.items():
    patch = mpatches.Patch(color=color, label=country, edgecolor='black', linewidth=0.5)
    legend_elements.append(patch)

# Add legend
plt.legend(handles=legend_elements,
           loc='upper right',
           fontsize=11,
           title="Participating Countries",
           title_fontsize=13,
           frameon=True,
           fancybox=True,
           shadow=True,
           borderpad=1)

# Set white background
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Adjust layout
plt.tight_layout()

# ==========================================
# NEW: Updated folder path for new structure
# ==========================================

# Get the script's directory and navigate to outputs/maps
script_dir = Path(__file__).parent  # 0_Project_Overview/scripts/
project_root = script_dir.parent.parent  # BENEFITS/
figures_folder = project_root / "0_Project_Overview" / "outputs" / "maps"

# Create the folder if it doesn't exist
figures_folder.mkdir(parents=True, exist_ok=True)
print(f"Saving figures to: {figures_folder}")

# Generate filename with timestamp (optional, for unique names)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"europe_participant_map_{timestamp}.png"

# Or use a simple filename (uncomment this line if you prefer)
# filename = "europe_participant_map.png"

# Full path for saving (UPDATED to use Path)
save_path = figures_folder / filename

# Save the figure
plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"Figure saved to: {save_path}")

# Show the plot
plt.show()