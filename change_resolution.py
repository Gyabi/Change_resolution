import cv2
import os
import numpy as np

def create_low_resolution_image(img_path, save_name, rate):
    """pathから画像を読み込み、rate倍の低解像度画像を保存する。

    Args:
        img_path (string): オリジナル画像のpath
        save_name (string): 保存する画像のファイル名(拡張子を含む)
        rate (float): 低解像度画像の解像度をrate倍にする。
    """
    img = cv2.imread(img_path)
    process_img = resolution_degradation_processing(img, rate)
    cv2.imwrite(os.path.join("./output", save_name), process_img)
    

def resolution_degradation_processing(img, rate):
    """入力画像をrate倍の低解像度画像に変換する。

    Args:
        img (np.array): オリジナル画像のnumpy配列
        rate (float): 低解像度画像の解像度をrate倍にする。

    Returns:
        np.array: 処理後のnumpy配列
    """
    # 元画像のサイズを取得
    original_height, original_width = img.shape[:2]
    print("オリジナル解像度:",original_height, "x", original_width)
    
    # 元画像サイズの出力用numpy配列を作成
    output_img = np.zeros((int(original_height), int(original_width), 3), dtype=np.uint8)
    
    # 作成する画像の分割を算出
    new_height = int(original_height * rate)
    new_width = int(original_width * rate)
    print("新規解像度:",new_height, "x", new_width)
    # 作成する画像のピクセル数を算出
    pixel_height = int(original_height / new_height)
    pixel_width = int(original_width / new_width)
    
    
    for height in range(new_height):
        for width in range(new_width):
            # 周辺の平均を取得
            average_color = img[pixel_height*height:pixel_height*(height+1), pixel_width*width:pixel_width*(width+1),:].mean(axis=(0,1))
            # outputに取得した平均値を反映
            output_img[pixel_height*height:pixel_height*(height+1), pixel_width*width:pixel_width*(width+1),:] = average_color
            
    return output_img
    
    
    
if __name__ == "__main__":
    create_low_resolution_image("./lena.jpg", "out.jpg", 0.5)
    # create_low_resolution_image("./test.png", "out2.jpg", 0.2)