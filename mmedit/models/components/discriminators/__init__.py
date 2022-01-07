# Copyright (c) OpenMMLab. All rights reserved.
from .deepfill_disc import DeepFillv1Discriminators
from .gl_disc import GLDiscs
from .light_cnn import LightCNN
from .modified_vgg import ModifiedVGG
from .multi_layer_disc import MultiLayerDiscriminator
from .patch_disc import PatchDiscriminator
<<<<<<< HEAD
from .smpatch_disc import SoftMaskPatchDiscriminator

__all__ = [
    'GLDiscs', 'ModifiedVGG', 'MultiLayerDiscriminator',
    'DeepFillv1Discriminators', 'PatchDiscriminator',
    'SoftMaskPatchDiscriminator'
=======
from .ttsr_disc import TTSRDiscriminator
from .unet_disc import UNetDiscriminatorWithSpectralNorm

__all__ = [
    'GLDiscs', 'ModifiedVGG', 'MultiLayerDiscriminator', 'TTSRDiscriminator',
    'DeepFillv1Discriminators', 'PatchDiscriminator', 'LightCNN',
    'UNetDiscriminatorWithSpectralNorm'
>>>>>>> 69c5df50969afdd941aa66a1eee84c548de46585
]
