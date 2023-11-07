\setupcode{
  importTool('GPmat')
  gpmatToolboxes
  randn('seed', 1e4);
  rand('seed', 1e4);
  lineWidth = 4;
  textWidth = 13;
  colWidth = 5;
  markerSize = 2;
  markerWidth = 4;
  markerType = 'kx';
  
  redColor = [1, 0, 0];
  greenColor = [0, 1, 0];
  blueColor = [0, 0, 1];
  magentaColor = [1, 0, 1];
  blackColor = [0, 0, 0];
  fillColor = [0.7 0.7 0.7];
  negative = false;
  if blackBackground
    negative = true;
    redColor = 1-redColor;
    greenColor = 1-greenColor;
    blueColor =  1-blueColor;
    magentaColor = 1-magentaColor;
    blackColor = 1- blackColor;
    fillColor = 1-fillColor;
  end
  directory = '\writeDiagramsDir/sysbio/';
}

###

ODE1 ARTIFICIAL EXAMPLE

\code{
load ../../../gpsim/matlab/demToyProblem7.mat

predt = [linspace(0, 18, 100)]';
figure(1), clf
order = [4 3 2];
lin1 = [];
colors = {blueColor, greenColor, redColor};
hold on;
for i = 1:length(order)
  lin1 = [lin1; plot(t, truey(:, order(i)-1), 'color', colors{i})];
end
set(gca, 'ylim', [0 8]);
xlim = get(gca, 'xlim');
ylim = get(gca, 'ylim')
line([xlim(1) xlim(1)], ylim, 'color', blackColor)
line(xlim, [ylim(1) ylim(1)], 'color', blackColor)

hold on
lin2 = [];
counter = 0;
presentOrder = 0;
for i = order
  presentOrder = presentOrder + 1;
  for j = 1:length(model.timesCell{i})
    counter = counter + 1;
    indices(counter, 1) = i;
    indices(counter, 2) = j;
    indices(counter, 3) = presentOrder;
  end
end
ind = [1];
tvals = cell(length(model.timesCell));
includeText = [];
for i = 1:size(indices, 1)
  offset = 0;
  for j = 1:indices(i, 1)-1
    offset = offset + length(model.timesCell{j});
  end
  ind = [ind indices(i, 2)+offset];
  tvals{indices(i, 1)} = [tvals{indices(i, 1)}; model.timesCell{indices(i, 1)}(indices(i, ...
                                                    2))];
  
  proteinKern = model.kern.comp{1};
  K = rbfKernCompute(proteinKern, 0, predt);
  counter = 0;
  for j=order
    counter = counter + 1;
    if ~isempty(tvals{j})
      K = [K; real(simXrbfKernCompute(model.kern.comp{j}, proteinKern, ...
                                      tvals{j}, predt))];
    end
  end  
  invK = pdinv(model.K(ind, ind));
  obsY = model.m(ind, 1);
  predF = K'*invK*obsY;
  varF = kernDiagCompute(proteinKern, predt) - sum(K.*(invK*K), 1)';
  
  figure(1)
  lin2 = [ plot(model.timesCell{indices(i, 1)}(indices(i, 2)), ...
               [repmat(NaN, 1, indices(i, 3)-1) model.y(ind(end) - 1)], 'x', ...
               'color', colors{indices(i, 3)})];
  set(lin1, 'lineWidth', 2);
  set(lin1, 'markersize', 10);
  set(lin2, 'lineWidth', 4);
  set(lin2, 'markersize', 10);
  %set(gca, 'fontname', 'arial', 'fontsize', 24, 'xlim', xlim, 'ylim', [0 8])
  fileName = ['toyGeneData' num2str(i)];
  printLatexPlot(fileName, directory, 0.4*textWidth);
  includeText = [includeText '###\n\n']
  includeText = [includeText '\includeimg{' directory fileName '}{45%}{}{left}'];
   
  figure(2), clf  
  hold on
  stdVals = sqrt(varF);
  fillColor = [0.7 0.7 0.7];
  patch([predt; predt(end:-1:1)], ...
        [predF; predF(end:-1:1)] ...
        + 2*[stdVals; -stdVals(end:-1:1)], ...
            fillColor,'edgecolor',fillColor)
  % fill(, ...
  %      fillColor,'EdgeColor',fillColor)
  lin = plot(t, truef, '-', 'color', blueColor);  
  lin = [lin plot(predt, predF, '-', 'color', blackColor)];
  set(lin, 'lineWidth', 4);
  set(lin, 'markersize', 10);
  %set(gca, 'fontname', 'arial', 'fontsize', 24, 'xlim', xlim)
  ylim = [-2 4];
  xlim = get(gca, 'xlim');
  set(gca, 'ylim', ylim)
  line([xlim(1) xlim(1)], ylim, 'color', blackColor)
  line(xlim, [ylim(1) ylim(1)], 'color', blackColor)
  fileName = ['groundTruthTFData' num2str(i)];
  printLatexPlot(fileName, directory, 0.4*textWidth);
  includeText = [includeText '\includeimg{' directory fileName '}{45%}{}{right}'];
end
    printLatexText(includeText, 'infer-tf-from-gene-text.md', directory)

}

include{\diagramsDir/sysbio/infer-tf-from-gene-text.md}

