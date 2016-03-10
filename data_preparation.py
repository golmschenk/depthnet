"""
Code for preparing data.
"""
import os
import h5py
import numpy as np


class DataPreparation:
    """
    A class for data preparation.
    """
    def convert_mat_file_to_numpy_file(self, mat_file_path, number_of_samples=None):
        """
        Generate image and depth numpy files from the passed mat file path.

        :param mat_file_path: The path to the mat file.
        :type mat_file_path: str
        :param number_of_samples: The number of samples to extract.
        :type number_of_samples: int
        """
        mat_data = h5py.File(mat_file_path, 'r')
        images = self.convert_mat_data_to_numpy_array(mat_data, 'images', number_of_samples=number_of_samples)
        depths = self.convert_mat_data_to_numpy_array(mat_data, 'depths', number_of_samples=number_of_samples)
        basename = os.path.basename(os.path.splitext(mat_file_path)[0])
        np.save(os.path.join('data', 'images_' + basename) + '.npy', images)
        np.save(os.path.join('data', 'depths_' + basename) + '.npy', depths)

    @staticmethod
    def convert_mat_data_to_numpy_array(mat_data, variable_name_in_mat_data, number_of_samples=None):
        """
        Converts a mat data variable to a numpy array.

        :param mat_data: The mat data containing the variable to be converted.
        :type mat_data: h5py.File
        :param variable_name_in_mat_data: The name of the variable to extract.
        :type variable_name_in_mat_data: str
        :param number_of_samples: The number of samples to extract.
        :type number_of_samples: int
        :return: The numpy array.
        :rtype: np.ndarray
        """
        mat_variable = mat_data.get(variable_name_in_mat_data)
        untransposed_array = np.array(mat_variable)
        if number_of_samples:
            untransposed_array = untransposed_array[:number_of_samples]
        return untransposed_array.transpose()


if __name__ == '__main__':
    data_preparation = DataPreparation()
    data_preparation.convert_mat_file_to_numpy_file('data/nyu_depth_v2_labeled.mat')
