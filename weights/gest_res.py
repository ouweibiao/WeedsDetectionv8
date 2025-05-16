from test_media.Path import get_abs_path, abs_path

if __name__ == '__main__':  # 确保该模块被直接运行时才执行以下代码
    print(abs_path('datasets/Weeds/weeds.yaml', path_type="parent"))
