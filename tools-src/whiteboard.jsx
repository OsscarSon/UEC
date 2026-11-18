import React from 'react';
import {createRoot} from 'react-dom/client';
import {Excalidraw} from '@excalidraw/excalidraw';
import '@excalidraw/excalidraw/index.css';
export function mountBoard(element,initial,onChange){
 const root=createRoot(element);let api;const theme=document.documentElement.dataset.theme==='dark'||(document.documentElement.dataset.theme!=='light'&&matchMedia('(prefers-color-scheme: dark)').matches)?'dark':'light';
 root.render(<Excalidraw langCode="zh-CN" theme={theme} aiEnabled={false} initialData={initial||{elements:[],appState:{viewBackgroundColor:'#ffffff'}}} excalidrawAPI={value=>{api=value;window.activeStudyBoard=value;}} onChange={(elements,appState,files)=>onChange({elements,appState:{viewBackgroundColor:appState.viewBackgroundColor,gridSize:appState.gridSize,gridStep:appState.gridStep,gridModeEnabled:appState.gridModeEnabled,scrollX:appState.scrollX,scrollY:appState.scrollY,zoom:appState.zoom},files})} UIOptions={{canvasActions:{loadScene:true,export:{saveFileToDisk:true},saveAsImage:true,toggleTheme:true},tools:{image:true}}}/>);
 return {unmount(){root.unmount();if(window.activeStudyBoard===api)window.activeStudyBoard=null;}};
}
