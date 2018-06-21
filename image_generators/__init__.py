from .wms import wmsImage
from .fileimage import fileImage


renderers = {
    'wms' : wmsImage,
    'imageFile' : fileImage
}