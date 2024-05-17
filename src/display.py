#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import os 
from collections import defaultdict
from pprint import pprint 


def rescale_bbox(bbox, rescale_factor, page_dimension): 
    return [
        bbox[0]*rescale_factor[0],                              # x_min
        (page_dimension["height"] - bbox[3])*rescale_factor[1], # y_min
        bbox[2]*rescale_factor[0],                              # x_max
        (page_dimension["height"] - bbox[1])*rescale_factor[1]  # y_max
    ]

def display_molecules_locations(pages, patent_entry, max_pages_per_row=1, max_pages_displayed=1000, highlight_smiles_list=[]):
    # Set display options
    font = ImageFont.truetype(os.path.dirname(__file__) + "/../data/fonts/calibri.ttf", 80)
    display_page_dimension = {"width": 2592, "height": 3509}
    class_color_palette = {
        "Clean": (0, 149, 255, 84),
        "Markush": (239, 25, 25, 84),
        "Trash": (0, 0, 0, 30)
    }
    highlight_smiles_counts = defaultdict(list)
    molecule_index = 0
    display_bloc = []
    for page_index in range(1, len(patent_entry['page-dimensions'])+1):
        if pages[page_index-1] == None:
            continue
        if page_index > max_pages_displayed:
            continue
        figures = [figure for figure in patent_entry["figures"] if (figure["page"] == page_index)]
        page_dimension = patent_entry['page-dimensions'][page_index - 1]
        rescale_factor = [
            display_page_dimension["width"]/page_dimension["width"],
            display_page_dimension["height"]/page_dimension["height"]
        ]

        # Display images locations and classes
        index_smiles_mapping = {} 
        page_image = pages[page_index - 1].resize((display_page_dimension["width"], display_page_dimension["height"]))
        draw = ImageDraw.Draw(page_image)
        for figure in figures:
            if not("class" in figure):
                continue

            bbox = rescale_bbox(figure["bbox"], rescale_factor, page_dimension)
            page_image_with_bbox = Image.new('RGBA', page_image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(page_image_with_bbox)
            outline = None
            if ("smiles" in figure) and (figure["smiles"]["value"] in highlight_smiles_list):
                outline = "Blue"
            draw.rectangle(bbox, width=10, fill=class_color_palette[figure["class"]], outline=outline) 

            if "smiles" in figure:
                # Display smiles
                bbox_pil = draw.textbbox((bbox[0], bbox[1]), str(molecule_index), font=font)
                draw.rectangle(bbox_pil, fill=(255, 255, 255, 120))
                draw.text((bbox[0], bbox[1]), str(molecule_index), fill="Blue", font=font)
                index_smiles_mapping[molecule_index] = figure["smiles"]["value"]
                molecule_index += 1
            
            page_image = Image.alpha_composite(page_image.convert("RGBA"), page_image_with_bbox)

        display_bloc.append({
            "page": page_image,
            "page_index": page_index,
            "smiles": index_smiles_mapping
        })
        if len(display_bloc) == max_pages_per_row:
            # Display page
            if max_pages_per_row == 1:
                plt.figure(figsize=(9,11))
            else:
                fig, axs = plt.subplots(1, max_pages_per_row, figsize=(20, 20))
            print("="*135)
            for i in range(len(display_bloc)):
                if max_pages_per_row == 1:
                    plt.axis("off")
                    plt.imshow(display_bloc[i]["page"])
                else:
                    axs[i].axis("off")
                    axs[i].imshow(display_bloc[i]["page"])
                # Display smiles
                print(f"Molecules in page {display_bloc[i]['page_index']}")
                for i2, smiles in display_bloc[i]["smiles"].items():
                    if smiles in highlight_smiles_list:
                        highlight_smiles_counts[smiles].append(display_bloc[i]['page_index'])
                        print(f"*{i2}: {smiles}*")
                    else:
                        print(f"{i2}: {smiles}")
            #plt.savefig(str(page_index) + ".png", dpi=300)
            plt.show()
            plt.close()
            display_bloc = []
    pprint(highlight_smiles_counts)

        