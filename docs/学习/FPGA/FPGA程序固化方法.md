# FPGA程序固化方法
- 参考：正点原子B站官方教学视频

为了固化程序，需要设置上电后快速启动，以及产生bin文件并写入bin文件到Flash。

### 设置上电后快速启动

为了实现FPGA上电后快速启动，在管脚约束文件中添加如下内容：
```xdc
#SPI 相关设置 用于上电后快速启动
set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]
set_property CONFIG_MODE SPIx4 [current_design]
set_property BITSTREAM.CONFIG.CONFIGRATE 50 [current_design]
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 3.3 [current_design]
# 设置未使用的引脚上拉，根据实际需要进行配置
set_property BITSTREAM.CONFIG.UNUSEDPIN PULLUP [current_design] 
```
### 设置Vivado生存bin文件的方法
- 点击设置
- 点击Project Setting下的Bitstream
- 勾选`-bit_file`后的单选框
- 点击ok
### 生成bin文件
- 点击`Generate Bitstream`生成bit流
- 在FPGA项目下的`runs\impl_1`文件夹中存在`.bin`格式的文件，即固化文件
### 生成MCS文件（可跳过）
- 选择菜单栏的`Tools`
- 选择下拉菜单的`Generate Memory Configuration File`选项
- 根据实际Flash大小配置`Custom Memory Size`，注意此处单位是==MB==
- 设置要生成的MCS文件路径和名称
- 由于约束语句里面是`SPIx4`，所以`Interface`选择`SPIx4`
- 选中`Load bitstream files`选项，在`Bitfile`中选择bit文件
- 选中：`Write checksum`、`Disable bit swapping`、`Overwrite`
- 复制`Command`命令，用于以后快速生成MCS文件
### 固化程序
- 点击`Open Hardware Manager`
- 选择菜单栏的`Tools`
- 选择下拉菜单的`Add Configuration Memory Device`选项
- 根据Flash型号进行配置
- 选择固化文件（bin或者MCS文件）
- 点击ok