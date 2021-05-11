(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[5],{3905:function(e,r,t){"use strict";t.d(r,{Zo:function(){return p},kt:function(){return f}});var o=t(7294);function n(e,r,t){return r in e?Object.defineProperty(e,r,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[r]=t,e}function l(e,r){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);r&&(o=o.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),t.push.apply(t,o)}return t}function a(e){for(var r=1;r<arguments.length;r++){var t=null!=arguments[r]?arguments[r]:{};r%2?l(Object(t),!0).forEach((function(r){n(e,r,t[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):l(Object(t)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(t,r))}))}return e}function i(e,r){if(null==e)return{};var t,o,n=function(e,r){if(null==e)return{};var t,o,n={},l=Object.keys(e);for(o=0;o<l.length;o++)t=l[o],r.indexOf(t)>=0||(n[t]=e[t]);return n}(e,r);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(o=0;o<l.length;o++)t=l[o],r.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(n[t]=e[t])}return n}var c=o.createContext({}),d=function(e){var r=o.useContext(c),t=r;return e&&(t="function"==typeof e?e(r):a(a({},r),e)),t},p=function(e){var r=d(e.components);return o.createElement(c.Provider,{value:r},e.children)},s={inlineCode:"code",wrapper:function(e){var r=e.children;return o.createElement(o.Fragment,{},r)}},u=o.forwardRef((function(e,r){var t=e.components,n=e.mdxType,l=e.originalType,c=e.parentName,p=i(e,["components","mdxType","originalType","parentName"]),u=d(t),f=n,m=u["".concat(c,".").concat(f)]||u[f]||s[f]||l;return t?o.createElement(m,a(a({ref:r},p),{},{components:t})):o.createElement(m,a({ref:r},p))}));function f(e,r){var t=arguments,n=r&&r.mdxType;if("string"==typeof e||n){var l=t.length,a=new Array(l);a[0]=u;var i={};for(var c in r)hasOwnProperty.call(r,c)&&(i[c]=r[c]);i.originalType=e,i.mdxType="string"==typeof e?e:n,a[1]=i;for(var d=2;d<l;d++)a[d]=t[d];return o.createElement.apply(null,a)}return o.createElement.apply(null,t)}u.displayName="MDXCreateElement"},2181:function(e,r,t){"use strict";t.r(r),t.d(r,{frontMatter:function(){return a},metadata:function(){return i},toc:function(){return c},default:function(){return p}});var o=t(2122),n=t(9756),l=(t(7294),t(3905)),a={sidebar_label:"world",title:"fido.world.world"},i={unversionedId:"reference/fido/world/world",id:"reference/fido/world/world",isDocsHomePage:!1,title:"fido.world.world",description:"World Objects",source:"@site/docs/reference/fido/world/world.md",sourceDirName:"reference/fido/world",slug:"/reference/fido/world/world",permalink:"/fido/docs/reference/fido/world/world",editUrl:"https://github.com/hojulian/fido/edit/documentation/docs/docs/reference/fido/world/world.md",version:"current",sidebar_label:"world",frontMatter:{sidebar_label:"world",title:"fido.world.world"},sidebar:"apiSidebar",previous:{title:"fido.world.racetrack",permalink:"/fido/docs/reference/fido/world/racetrack"},next:{title:"fido.config",permalink:"/fido/docs/reference/fido/config"}},c=[{value:"World Objects",id:"world-objects",children:[]}],d={toc:c};function p(e){var r=e.components,t=(0,n.Z)(e,["components"]);return(0,l.kt)("wrapper",(0,o.Z)({},d,t,{components:r,mdxType:"MDXLayout"}),(0,l.kt)("h2",{id:"world-objects"},"World Objects"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"},"class World(ABC,  WorldProtocol)\n")),(0,l.kt)("p",null,"Represents a world."),(0,l.kt)("p",null,"Currently this is only compatible with Gazebo."),(0,l.kt)("h4",{id:"add"},"add"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | add(robot: Robot, x=0, y=0, z=0) -> None\n")),(0,l.kt)("p",null,"Add a robot to the world."),(0,l.kt)("p",null,"Internally, this is converted into a gazebo_ros spawn_model\ncall."),(0,l.kt)("h4",{id:"prepare_robots"},"prepare","_","robots"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | prepare_robots() -> None\n")),(0,l.kt)("p",null,"Prepare prepares all the robots in the world."),(0,l.kt)("h4",{id:"set_simulation"},"set","_","simulation"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | set_simulation(simulation) -> None\n")),(0,l.kt)("p",null,"Set the parent simulation."),(0,l.kt)("h4",{id:"remove"},"remove"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | remove(robot: Robot) -> None\n")),(0,l.kt)("p",null,"Remove a robot from the world."),(0,l.kt)("p",null,"Internally, this is converted into a gazebo_ros delete_model\ncall."),(0,l.kt)("h4",{id:"robots"},"robots"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | robots() -> List[Robot]\n")),(0,l.kt)("p",null,"Returns a list of robots."),(0,l.kt)("h4",{id:"ros"},"ros"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | ros() -> Ros\n")),(0,l.kt)("p",null,"Return internal ROS client."),(0,l.kt)("h4",{id:"export_files"},"export","_","files"),(0,l.kt)("pre",null,(0,l.kt)("code",{parentName:"pre",className:"language-python"}," | export_files(path, package, rosbridge_port) -> None\n")),(0,l.kt)("p",null,"Export files to a given file."),(0,l.kt)("p",null,"Internally, .rosinstall file is exported to the root of the directory.\nThe launch file is exported to $PATH/src/$PACKAGE/launch."))}p.isMDXComponent=!0}}]);