# MEDIA
# media/brand_mango/some image.jpg
def brand_name_directory_path(instance, filename):
    return "brands/brand_{0}/{1}".format(instance.title.lower(), filename)


def product_name_directory_path(instance, filename):
    return "apps/products/{0}".format(filename)


def get_sizes():
    size = []
    for i in range(38, 60, 2):
        size.append((str(i), (str(i))))
    size = tuple(size)
    return size
