# 图形的绘制

# 格式与注释

# 图片处理

# 打印和导出
## 导出
### exportgraphics command
常用指令形式

    exportgraphics(obj,filename)
    %obj表示指定的图形对象内容
    exportgraphics(obj,filename,Name,Value)
    %Name和Value表示其他导出参数和对应选项
    
expample 01

    plot(rand(5,5))
    ax=gca
    exportgraphics(ax,'nameoffile.jpg')


### copygraphics command
### exportapp command
### getframe command
### saveas command
## 打印
### print command
### orient command
# 图形对象
## 图形对象属性
## 图形对象标识
### 获取当前对象
gca command 表示当前坐标区或图  
gcf command  
gcbf command  
gcbo command  
groot command  
### 搜索对象
### 确定对象类型
### 创建、复制或删除对象
## 图形对象编成
# 图形性能
