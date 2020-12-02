from ssd.modeling import registry
from .vgg import VGG
from .mobilenet import MobileNetV2
from .efficient_net import EfficientNet
from .mobilenetv3 import MobileNetV3
from .light_ssd import Light_VGG
from .enrich_vgg import Enrich_VGG

__all__ = ['build_backbone', 'Light_VGG','Enrich_VGG','VGG', 'MobileNetV2', 'EfficientNet', 'MobileNetV3']


def build_backbone(cfg):
    return registry.BACKBONES[cfg.MODEL.BACKBONE.NAME](cfg, cfg.MODEL.BACKBONE.PRETRAINED)
