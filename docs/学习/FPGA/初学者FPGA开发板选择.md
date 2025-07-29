---
authors:
  - TFC
tags:
  - 学习
  - FPGA
  - 教程
---
# 初学者FPGA开发板选择
- 参考：
	- [如何选择适合初学者的FPGA开发板？ | 嵌入式开发](https://www.duwenxian.com/qianrushi/archives/16)
	- [FPGA开发板的选择，Altera还是Xilinx公司的板子呢？ 新手求推荐板子型号，最好有购买链接？](https://www.zhihu.com/tardis/bd/ans/3155696284)
	- [Xilinx之FPGA器件系列简介 - 知乎](https://zhuanlan.zhihu.com/p/622334501)
	- [10分钟了解Xilinx 7系列FPGA - 知乎](https://zhuanlan.zhihu.com/p/630914181)
	- [XILINX FPGA简介-型号系列分类参考 - 知乎](https://zhuanlan.zhihu.com/p/612817485)

最近想要入门FPGA，需要选择合适的开发板。就在网上查找了一些资料，方便自己进行选择。因为我偏向于Xilinx，所以就更偏向于Xilinx的内容。

如何选择开发板，关键还是要根据自己的实际需求而进行选择。

### FPGA芯片制造商
- Xilinx、Altera是主要的FPGA制造商，Xilinx重在高端产品线，而Altera重在中低端产品线。
- 初学阶段可以选用Altera的开发板，价格便宜，学习资料丰富，有了一定的经验以后，可以用Xilinx的开发板。
- Altera对应开发软件为Quartus，Xilinx对应开发软件为Vivado(之前为ISE，更新到14.7后不再更新）。
### Xilinx芯片命名规则
#### 按照代数分
按照产品代数，分为6代，7代，Ultrascale，Ultrascale+，Versal。
6代是较早的器件，现在基本是7代及之后的产品，最新的一代是Versal，主要用于人工智能领域。
#### 按照系列分
- 6代FPGA芯片主要分为Spartan、Virtex。

- 7代FPGA芯片主要分为Spartan、Artix、Kintex和Virtex四个系列。
	- Spartan-7系列是入门级产品，有着最低的价格、功耗和尺寸，适用于低端应用。
	- Artix-7系列增加了串行收发器和DSP功能，具有更大的逻辑容量，适合逻辑稍微复杂的中低端应用。
	- Kintex-7系列在硬核数量和逻辑容量方面都表现优异，适用于中低端和部分高端应用。
	- Virtex-7系列在高端应用中使用，对于中低端应用来说过于强大而显得大材小用。

- Ultrascale： KINTEX、VIRTEX

- Ultrascale+： ARTIX、KINTEX、VIRTEX、ZYNQ。（ZYNQ表示集成了arm芯片）

- Versal： AI Core、AI Edge、Prime、Premium，主要用于AI领域，使用了ACAP自适应加速平台，采用异构加速，在软件和硬件级别上进行动态自定义来适应各种应用场景。

### 开发板选择
- 使用Altera芯片的开发板要比Xilinx的便宜。
- 如果采用Xilinx的芯片，7代以后的芯片，可以使用Vivado开发，6代及以前的芯片，需要使用ISE软件开发，但是ISE软件已经不再更新，在win11上存在兼容问题。所以虽然6代芯片便宜，但是不推荐。
- ZYNQ表示集成了Arm芯片，但是初学者可能不会用到，所以可以买不带有ZYNQ的芯片，减少购买成本。

