# The goal of this script was to download get data around 3d models i.e. image thumbnail data to then show to a llm to describe as well as to render in ascii
# It is unseen, if this data procurement method is not likely to support a high quality training run. On the one hand ascii renderings have been seen to lead to new capabilities, of which potentially better results than vision encoders, however the quality and percision of the ascii data would likely be just as important. 
import requests
import json
import xmltodict
import os
from pathlib import Path

def dfs_target_users():
    # Define the initial target user IDs (UIDs) to start the search
    # You can uncomment the other UID examples to search for different users
    # uids = ['820c0206d14d4c76a2aff53625bb1af8'] # strisunshine
    uids = ['e9db551b564149808335556d521a9f51'] # WirtualneMuzeaMalopolski

    # Initialize an empty dictionary to store the target user information
    target_users = {}

    # Set the initial recursion level
    recurse_level = 1

    # Start the depth-first search loop
    while recurse_level >= 0:
        # Initialize a list to store the new UIDs to be visited in the next iteration
        new_uids = []

        # Iterate through the current UIDs
        for uid in uids:
            # Construct the API URL to retrieve the followed users for the current UID
            url = f"https://api.sketchfab.com/v3/users/{uid}/followings"

            # Make a GET request to the API and retrieve the response
            response = requests.get(url)

            # Iterate through the results and collect the information about the followed users
            for user_info in response.json()['results']:
                # Get the UID of the followed user
                new_uid = user_info['uid']

                # Add the new UID to the list of new UIDs, if it's not already there
                if new_uid not in new_uids:
                    new_uids.append(new_uid)

                # Add the followed user's information to the target_users dictionary
                target_users[new_uid] = {
                    'username': user_info['username'],
                    'models_url': user_info['modelsUrl'],
                }

                # If the target_users dictionary has reached 150 entries, break out of the loop
                if len(target_users) >= 150:
                    break

            # If the target_users dictionary has reached 150 entries, break out of the loop
            if len(target_users) >= 150:
                break

        # Update the UIDs list with the new UIDs
        uids = new_uids

        # Decrement the recursion level
        recurse_level -= 1

    # Return the target_users dictionary
    return target_users

def get_thumb_image_infos():
    target_users = dfs_target_users()
    usernames = [user_info['username'] for user_info in target_users.values()]
    print(f"fetching images from {usernames}")

    thumb_image_info = {}
    for uid, user_info in target_users.items():
        models_url = user_info["models_url"]
        response = requests.get(models_url)
        images_info = response.json()
        if 'results' not in images_info:
            continue
        for image_info in images_info['results']:
            if not image_info['isDownloadable']:
                continue
            image_id = image_info['uid']
            thumb_url = image_info['thumbnails']['images'][0]['url']
            thumb_size = image_info['thumbnails']['images'][0]['size']
            for thumbnail in image_info['thumbnails']['images']:
                if thumbnail['size'] <= 20000:
                    thumb_url = thumbnail['url']
                    thumb_size = thumbnail['size']
                    break
            thumb_image_info[image_id] = {
                'userid': uid,
                'thumb_url': thumb_url,
                'size': thumb_size,
            }
    breakpoint()
    return thumb_image_info

def download_image():
    thumb_image_info = get_thumb_image_infos()
    # thumb_image_info = {
    #     '128d863ab5c8467f80939cabe8b3fc34': {
    #         "thumb_url": "https://media.sketchfab.com/models/c269c1cbac29486b969f6a926612298e/thumbnails/2d40b6a2d45e439f963e7769d78d6978/10bceeaaad504b84be56a28ef6d4158e.jpeg",
    #         "size": 12345
    #     }
    # }
    i = 0
    for image_id, info in thumb_image_info.items():
        url = info['thumb_url']
        size = info['size']
        img_data = requests.get(url).content
        img_file_path = f'/Users/wentingwang/3Dasset_thumbnails/{image_id}.jpg'
        i += 1
        if Path(img_file_path).exists():
            continue
        print(f"{i}: downloading {image_id} from {url}")
        with open(img_file_path, 'wb') as handler:
            handler.write(img_data)

def gen_image_info_json():
    images = []
    for root, d_names, f_names  in os.walk("/Users/wentingwang/3Dasset_thumbnails/"):
        for file in f_names:
            image_id, ext = os.path.splitext(file)
            stats = os.stat(f"{root}/{file}")
            if ext == '.jpg':
                images.append({
                    "id": image_id,
                    "size": stats.st_size,
                })
    images.sort(key=lambda x:x['size'], reverse = True)
    print(f"there are total {len(images)} images")
    with open('/Users/wentingwang/3Dasset_thumbnails/downloaded_images_meta.json', 'w') as f:
        json.dump(images, f)

download_image()
gen_image_info_json()
