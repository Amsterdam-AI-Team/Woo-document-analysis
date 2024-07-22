"""Paths when running on Azure (AML)"""

HUGGING_CACHE = "/home/azureuser/cloudfiles/code//hugging_cache"

# Main folders
raadsinformatie_in_folder = "/home/azureuser/cloudfiles/code/blobfuse/raadsinformatie"
raadsinformatie_out_folder = (
    "/home/azureuser/cloudfiles/code/blobfuse/raadsinformatie/processed_data/woo_qa"
)

woo_sources = {
    "raadsinformatie": f"{raadsinformatie_in_folder}/raadsinformatie/search_results/woo_queries/manual/",
    "openamsterdam": f"{raadsinformatie_in_folder}/open.amsterdam/woo_queries/",
    "amsterdam.nl": f"{raadsinformatie_in_folder}/amsterdam.nl/",
}
