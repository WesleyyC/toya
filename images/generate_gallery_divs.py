""" 
please run within ./images:

python generate_gallery_divs.py > gallery_divs.txt
"""
import os

GALLERY_DIR = ['gallery', 'with-friends']

TEMPLATE = '<div class="item brand col-6 col-sm-6 col-md-6 col-lg-4 col-xl-4 mb-4">\n<a href="{}" class="item-wrap" data-fancybox="gal">\n<span class="icon-search2"></span>\n<img class="img-fluid" src="{}">\n</a>\n</div>'

for g_dir in GALLERY_DIR:
	for p in os.listdir(g_dir):
		if not p.startswith('.'):
			p = os.path.join('images', g_dir, p)
			print(TEMPLATE.format(p, p))

