% Demo for Amazon seminar 2016
% Code needed at:
% https://github.com/SheffieldML/multigp
% https://github.com/SheffieldML/hgplvm
% https://github.com/SheffieldML/hsvargplvm
% https://github.com/SheffieldML/GPmat
% and dependencies

importTool('multigp')
multigpToolboxes
clear all, close all
demAistats
pause

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