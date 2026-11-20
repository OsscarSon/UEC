import {use,init,getInstanceByDom,dispose} from 'echarts/core';
import {HeatmapChart,BarChart} from 'echarts/charts';
import {GridComponent,TooltipComponent,VisualMapComponent,LegendComponent,AriaComponent,GraphicComponent} from 'echarts/components';
import {CanvasRenderer} from 'echarts/renderers';
use([HeatmapChart,BarChart,GridComponent,TooltipComponent,VisualMapComponent,LegendComponent,AriaComponent,GraphicComponent,CanvasRenderer]);
export {init,getInstanceByDom,dispose};
