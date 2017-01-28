% Demo for MLSS Arequipa seminar 2016
% Code needed at:de
% https://github.com/SheffieldML/hgplvm
% https://github.com/SheffieldML/hsvargplvm
% https://github.com/SheffieldML/GPmat
% and dependencies


importTool('hgplvm')
hgplvmToolboxes
clear all, close all
load demWalkRun1
hgplvmHierarchicalVisualise(model, visualiseNodes, depVisData)
pause

importTool('hsvargplvm')
hsvargplvmToolboxes
clear all, close all
demDigitsDemonstration