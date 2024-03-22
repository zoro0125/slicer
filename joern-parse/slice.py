from gen_cpg import *
# from neo4j_admin_generator import *
# import neo4jhandler
# import os
# import subprocess
# import neo4j_connect
# from reader import *
# import logging

if __name__ == '__main__':
    c_path = 'C:\exp_data\exp_data\c_data_without_comment\\'
    cpp_path = 'C:\exp_data\exp_data\cpp_data_without_comment\\'
    ##  1、generate cpg.bin
    gen_cpg_bin(c_path)
    # gen_cpg_bin(cpp_path)
    # ##  2、transfer csv
    # neo4jcsv_export('C:\Mine\PythonProject\joern\data\cpg_bin')
    ##  4、import csv to neo4j database and export sliced graph(json)


    # csv_path = ''
    # for directory in os.listdir(csv_path):
    #
    #
    #     whole_csv_path = os.path.join(csv_path, directory)
    #     import_inst = generator(whole_csv_path)
    #     subprocess.run(import_inst, shell=True)
    #
    #     neo4jhandler.neo4j_start()                                             ## 导入之前数据库必须关闭
    #
    #     root_dir_lines = 'C:\exp_data\exp_data\slice_dir_0313\\bad\\'
    #     lines = get_lines_from_txt(root_dir_lines, directory)
    #     neo4j_connect.get_nodes_by_lines(lines, directory, 'bad')
    #
    #     root_dir_lines = 'C:\exp_data\exp_data\slice_dir_0313\\good\\'
    #     lines = get_lines_from_txt(root_dir_lines, directory)
    #     neo4j_connect.get_nodes_by_lines(lines, directory, 'good')
    #
    #     neo4j_connect.clear_all_data()                                         ## 清除数据库
    #
    #     neo4jhandler.neo4j_stop()

    ##





