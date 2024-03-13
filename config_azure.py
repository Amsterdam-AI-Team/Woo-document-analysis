"""Paths when running on Azure (AML)"""

HUGGING_CACHE = "/home/azureuser/cloudfiles/code//hugging_cache"

# Main folders
in_folder = "/home/azureuser/cloudfiles/code/blobfuse/raadsinformatie"
out_folder = "/home/azureuser/cloudfiles/code/blobfuse/raadsinformatie/processed_data/woo_qa"

woo_sources = {
    "raadsinformatie": f"{in_folder}/raadsinformatie/search_results/woo_queries/",
    "openamsterdam": f"{in_folder}/open.amsterdam/woo_queries/",
    "amsterdam.nl": f"{in_folder}/amsterdam.nl/",
}
