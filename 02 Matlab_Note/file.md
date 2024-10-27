### FCSANF
```matlab
A = fscanf (fileID, formatSpec)
A = fscanf (fileID, formatspe, sizeA)
[A, count] = fscanf (__)
```
* ```fileID```用文件标识符指示，使用```fopen```打开文件，指定字符编码，以获取```fileID```值，读取文件后使用```fclose(fileID)```来关闭文件。

### 正态分布
* 通过对样本数据进行概率分布拟合```fitdist```，或者通过指定参数值```makedist```来创建概率分布对象```NormalDistribution```，然后使用对象函数来计算分布、生成随机数等。