#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')

birds = ['rooster', 'ostrich', 'lark', ]

zoo += birds

zoo.remove('elephant')

print(zoo.index('lion') + 1)
print(zoo.index('lark') + 1)
print(zoo)

