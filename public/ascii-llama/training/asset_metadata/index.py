# training/AssetMetadata/index.py
# 05/13/24 eca

import struct
import json

def extract_glb_metadata(file_path):
    """
    Extracts metadata from a GLB file.

    Args:
        file_path (str): The path to the GLB file.

    Returns:
        dict: A dictionary containing the extracted metadata.
    """
    with open(file_path, 'rb') as f:
        # Read the GLB header
        magic = f.read(4)
        if magic != b'glTF':
            raise ValueError('Invalid GLB file format')

        version = struct.unpack('<I', f.read(4))[0]
        if version != 2:
            raise ValueError('Unsupported GLB version')

        length = struct.unpack('<I', f.read(4))[0]

        # Read the JSON chunk
        json_length = struct.unpack('<I', f.read(4))[0]
        json_type = f.read(4)
        if json_type != b'JSON':
            raise ValueError('Invalid JSON chunk')

        json_data = f.read(json_length).decode('utf-8')
        json_obj = json.loads(json_data)

        # Extract metadata from the JSON object
        metadata = {
            'asset': json_obj['asset'],
            'scene': json_obj['scene'],
            'scenes': json_obj['scenes'],
            'nodes': json_obj['nodes'],
            'meshes': json_obj['meshes'],
            'materials': json_obj['materials'],
            'textures': json_obj['textures'],
            'images': json_obj['images'],
            'accessors': json_obj['accessors'],
            'bufferViews': json_obj['bufferViews'],
            'buffers': json_obj['buffers']
        }

        return metadata
# example usage:
# metadata = extract_glb_metadata('/Users/ebowwa/simulation/public/models/glb/picture_frame.glb')
# print(metadata)