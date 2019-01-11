import os
import pandas
import logging
import numpy as np
import cv2
import SimpleITK as sitk
from radiomics import featureextractor
from PIL import Image

source_path = './source.nii.gz'
mask_path = './mask.nii.gz'
output_path = './features.csv'
def featureExtract(var):

    params_path = os.path.abspath('Params.yaml')
    extractor = featureextractor.RadiomicsFeaturesExtractor(params_path)
    results = pandas.DataFrame()
    try:
        image_path = var.im_path
        image_name = var.im_path.split('\\')
        image_name = image_name[-1]
        print(image_name)
        im = cv2.imread(image_path)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        im = cv2.resize(im, (256,256))
        mask = np.ones([256,256])

        im = sitk.GetImageFromArray([np.asarray(im)])
        mask = sitk.GetImageFromArray([np.asarray(mask)])

        sitk.WriteImage(im, source_path)
        sitk.WriteImage(mask, mask_path)

        print('fdssssssssssssssssssssssssssssssssss')
        featureVector = pandas.Series(extractor.execute(source_path, mask_path))
        featureVector.name = image_name
        results = results.join(featureVector, how='outer')
        results = results.T
        drop_dp = results.filter(regex=('diagnostics.*'))
        results = results.drop(drop_dp.columns, axis=1)
        results.to_csv(output_path, encoding='utf_8_sig')

    except Exception as e:
        logging.exception(e)