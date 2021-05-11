(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[171],{3905:function(e,t,r){"use strict";r.d(t,{Zo:function(){return c},kt:function(){return d}});var n=r(7294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var s=n.createContext({}),u=function(e){var t=n.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},c=function(e){var t=u(e.components);return n.createElement(s.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},m=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,i=e.originalType,s=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),m=u(r),d=o,f=m["".concat(s,".").concat(d)]||m[d]||p[d]||i;return r?n.createElement(f,a(a({ref:t},c),{},{components:r})):n.createElement(f,a({ref:t},c))}));function d(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=r.length,a=new Array(i);a[0]=m;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:o,a[1]=l;for(var u=2;u<i;u++)a[u]=r[u];return n.createElement.apply(null,a)}return n.createElement.apply(null,r)}m.displayName="MDXCreateElement"},3850:function(e,t,r){"use strict";r.r(t),r.d(t,{frontMatter:function(){return a},metadata:function(){return l},toc:function(){return s},default:function(){return c}});var n=r(2122),o=r(9756),i=(r(7294),r(3905)),a={sidebar_label:"simulator",title:"fido.simulation.simulator"},l={unversionedId:"reference/fido/simulation/simulator",id:"reference/fido/simulation/simulator",isDocsHomePage:!1,title:"fido.simulation.simulator",description:"Simulator Objects",source:"@site/docs/reference/fido/simulation/simulator.md",sourceDirName:"reference/fido/simulation",slug:"/reference/fido/simulation/simulator",permalink:"/fido/docs/reference/fido/simulation/simulator",editUrl:"https://github.com/hojulian/fido/edit/documentation/docs/docs/reference/fido/simulation/simulator.md",version:"current",sidebar_label:"simulator",frontMatter:{sidebar_label:"simulator",title:"fido.simulation.simulator"},sidebar:"apiSidebar",previous:{title:"fido.simulation.simulation",permalink:"/fido/docs/reference/fido/simulation/simulation"},next:{title:"fido.world.racetrack",permalink:"/fido/docs/reference/fido/world/racetrack"}},s=[{value:"Simulator Objects",id:"simulator-objects",children:[]}],u={toc:s};function c(e){var t=e.components,r=(0,o.Z)(e,["components"]);return(0,i.kt)("wrapper",(0,n.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"simulator-objects"},"Simulator Objects"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"},"class Simulator(ABC,  SimulatorProtocol)\n")),(0,i.kt)("p",null,"Represents a simulator."),(0,i.kt)("p",null,"A simulator provides a ROS compatible physics engine for running a\nsimulation."),(0,i.kt)("p",null,"Currently, there is only one supported simulator implementation: Gazebo."),(0,i.kt)("h4",{id:"set_simulation"},"set","_","simulation"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"}," | set_simulation(simulation) -> None\n")),(0,i.kt)("p",null,"Set the parent simulation."),(0,i.kt)("h4",{id:"start"},"start"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | start() -> None\n")),(0,i.kt)("p",null,"Start the simulator."),(0,i.kt)("p",null,"This starts the clock of the simulator."),(0,i.kt)("h4",{id:"stop"},"stop"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | stop() -> None\n")),(0,i.kt)("p",null,"Pause the simulator."),(0,i.kt)("p",null,"This will stop the simulation time as well."),(0,i.kt)("h4",{id:"reset"},"reset"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | reset() -> None\n")),(0,i.kt)("p",null,"Reset the simulator."),(0,i.kt)("p",null,"This will cause the simulator to reset itself to its original state.\nIt allows the simulator to reset without doing a destroy() and start().\nThis is useful in machine learning applications where each iteration\nrequires a fresh state."),(0,i.kt)("p",null,"The reset behavior depends on the simulator\u2019s implementation."),(0,i.kt)("h4",{id:"view"},"view"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | view() -> IFrame\n")),(0,i.kt)("p",null,"Visualize the simulator view."),(0,i.kt)("p",null,"This will display the view in a ",(0,i.kt)("inlineCode",{parentName:"p"},"IPython.core.display.display"),". This is\ncompatible with Jupyter notebook."),(0,i.kt)("p",null,"Currently, there is no way to adjust the view just yet."),(0,i.kt)("h4",{id:"time"},"time"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre",className:"language-python"}," | @abstractmethod\n | time() -> float\n")),(0,i.kt)("p",null,"Return the simulator time."))}c.isMDXComponent=!0}}]);