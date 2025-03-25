import pandas as pd
from matplotlib_venn import venn3
import matplotlib.pyplot as plt

# Read the CSV files
zulip_cwes = pd.read_csv('unique_cwes_report_zulip.csv')['UniqueCWEs'].str.split(',').explode().str.strip().unique()
scrapy_cwes = pd.read_csv('unique_cwes_report_scrapy.csv')['UniqueCWEs'].str.split(',').explode().str.strip().unique()
yt_dlc_cwes = pd.read_csv('unique_cwe_report_youtube-dlc.csv')['UniqueCWEs'].str.split(',').explode().str.strip().unique()

# Convert to sets for set operations
zulip_set = set(zulip_cwes)
scrapy_set = set(scrapy_cwes)
yt_dlc_set = set(yt_dlc_cwes)

# Calculate intersections and differences
common_all = zulip_set & scrapy_set & yt_dlc_set
zulip_only = zulip_set - (scrapy_set | yt_dlc_set)
scrapy_only = scrapy_set - (zulip_set | yt_dlc_set)
yt_dlc_only = yt_dlc_set - (zulip_set | scrapy_set)
zulip_scrapy = (zulip_set & scrapy_set) - yt_dlc_set
zulip_ytdlc = (zulip_set & yt_dlc_set) - scrapy_set
scrapy_ytdlc = (scrapy_set & yt_dlc_set) - zulip_set

# Venn diagram visualization
venn_labels = {
    '100': f"Zulip Only\n({len(zulip_only)})\n{', '.join(zulip_only)}",
    '010': f"Scrapy Only\n({len(scrapy_only)})\n{', '.join(scrapy_only)}",
    '001': f"youtube-dlc Only\n({len(yt_dlc_only)})\n{', '.join(yt_dlc_only)}",
    '110': f"Zulip & Scrapy\n({len(zulip_scrapy)})\n{', '.join(zulip_scrapy)}",
    '101': f"Zulip & youtube-dlc\n({len(zulip_ytdlc)})\n{', '.join(zulip_ytdlc)}",
    '011': f"Scrapy & youtube-dlc\n({len(scrapy_ytdlc)})\n{', '.join(scrapy_ytdlc)}",
    '111': f"All 3 Repos\n({len(common_all)})\n{', '.join(common_all)}"
}

plt.figure(figsize=(10, 8))
venn_diagram = venn3([zulip_set, scrapy_set, yt_dlc_set], ('Zulip', 'Scrapy', 'youtube-dlc'))

# Set custom labels with CWEs
for region in venn_labels:
    venn_diagram.get_label_by_id(region).set_text(venn_labels[region])

plt.title("CWE Overlap Between Zulip, Scrapy, and youtube-dlc")
plt.show()
