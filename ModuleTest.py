# -*- coding: utf-8 -*-
# @Time    : 08/10/2018
# @Author  : Elias Andrade

import core

if __name__ == '__main__':
    core.face_merge(src_img='images/destino.jpg',
                    dst_img='images/origem.jpg',
                    out_img='images/resultado.jpg',
                    face_area=[50, 30, 500, 485],
                    alpha=0.75,
                    k_size=(15, 10),
                    mat_multiple=0.95)
