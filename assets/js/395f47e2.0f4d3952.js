(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[6801],{3905:function(e,t,o){"use strict";o.d(t,{Zo:function(){return d},kt:function(){return p}});var r=o(67294);function n(e,t,o){return t in e?Object.defineProperty(e,t,{value:o,enumerable:!0,configurable:!0,writable:!0}):e[t]=o,e}function a(e,t){var o=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),o.push.apply(o,r)}return o}function i(e){for(var t=1;t<arguments.length;t++){var o=null!=arguments[t]?arguments[t]:{};t%2?a(Object(o),!0).forEach((function(t){n(e,t,o[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(o)):a(Object(o)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(o,t))}))}return e}function l(e,t){if(null==e)return{};var o,r,n=function(e,t){if(null==e)return{};var o,r,n={},a=Object.keys(e);for(r=0;r<a.length;r++)o=a[r],t.indexOf(o)>=0||(n[o]=e[o]);return n}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)o=a[r],t.indexOf(o)>=0||Object.prototype.propertyIsEnumerable.call(e,o)&&(n[o]=e[o])}return n}var c=r.createContext({}),u=function(e){var t=r.useContext(c),o=t;return e&&(o="function"==typeof e?e(t):i(i({},t),e)),o},d=function(e){var t=u(e.components);return r.createElement(c.Provider,{value:t},e.children)},s={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},m=r.forwardRef((function(e,t){var o=e.components,n=e.mdxType,a=e.originalType,c=e.parentName,d=l(e,["components","mdxType","originalType","parentName"]),m=u(o),p=n,f=m["".concat(c,".").concat(p)]||m[p]||s[p]||a;return o?r.createElement(f,i(i({ref:t},d),{},{components:o})):r.createElement(f,i({ref:t},d))}));function p(e,t){var o=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var a=o.length,i=new Array(a);i[0]=m;var l={};for(var c in t)hasOwnProperty.call(t,c)&&(l[c]=t[c]);l.originalType=e,l.mdxType="string"==typeof e?e:n,i[1]=l;for(var u=2;u<a;u++)i[u]=o[u];return r.createElement.apply(null,i)}return r.createElement.apply(null,o)}m.displayName="MDXCreateElement"},17191:function(e,t,o){"use strict";o.r(t),o.d(t,{frontMatter:function(){return i},metadata:function(){return l},toc:function(){return c},default:function(){return d}});var r=o(22122),n=o(19756),a=(o(67294),o(3905)),i={},l={unversionedId:"advanced",id:"advanced",isDocsHomePage:!1,title:"Advanced Features",description:"Simulation",source:"@site/docs/advanced.md",sourceDirName:".",slug:"/advanced",permalink:"/fido/docs/advanced",editUrl:"https://github.com/hojulian/fido/edit/documentation/docs/docs/advanced.md",version:"current",frontMatter:{},sidebar:"mainSidebar",previous:{title:"Concepts",permalink:"/fido/docs/concepts"},next:{title:"Contributing to Fido",permalink:"/fido/docs/contributing"}},c=[{value:"Simulation",id:"simulation",children:[{value:"Custom Docker Image",id:"custom-docker-image",children:[]}]},{value:"World",id:"world",children:[{value:"Custom World",id:"custom-world",children:[]}]},{value:"Robot",id:"robot",children:[{value:"Custom Robot",id:"custom-robot",children:[]}]}],u={toc:c};function d(e){var t=e.components,o=(0,n.Z)(e,["components"]);return(0,a.kt)("wrapper",(0,r.Z)({},u,o,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h2",{id:"simulation"},"Simulation"),(0,a.kt)("h3",{id:"custom-docker-image"},"Custom Docker Image"),(0,a.kt)("p",null,"By default, simulation uses ",(0,a.kt)("a",{parentName:"p",href:"https://github.com/hojulian/fido-image/blob/master/base/Dockerfile"},(0,a.kt)("inlineCode",{parentName:"a"},"cosi119/fido-simulation:base"))," as the base image. This image includes all the needed tools for running a simulation with the Gazebo simulator."),(0,a.kt)("p",null,"Base image's configuration:"),(0,a.kt)("ul",null,(0,a.kt)("li",{parentName:"ul"},"Ubuntu 18.04"),(0,a.kt)("li",{parentName:"ul"},"ROS Melodic"),(0,a.kt)("li",{parentName:"ul"},"NoVNC @ port 6080")),(0,a.kt)("p",null,"You can implement your own custom image by extending the base image:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-dockerfile",metastring:'title="Dockerfile"',title:'"Dockerfile"'},"FROM cosi119/fido-simulation:base\n\n# ...\n")),(0,a.kt)("h2",{id:"world"},"World"),(0,a.kt)("h3",{id:"custom-world"},"Custom World"),(0,a.kt)("p",null,"Fido supports custom worlds. To create a world, simply implements ",(0,a.kt)("a",{parentName:"p",href:"./reference/fido/world/world"},(0,a.kt)("inlineCode",{parentName:"a"},"World")),"."),(0,a.kt)("p",null,"See ",(0,a.kt)("a",{parentName:"p",href:"./reference/fido/world/racetrack"},(0,a.kt)("inlineCode",{parentName:"a"},"RaceTrack"))," for an example implementation."),(0,a.kt)("h2",{id:"robot"},"Robot"),(0,a.kt)("h3",{id:"custom-robot"},"Custom Robot"),(0,a.kt)("p",null,"Fido supports creation of custom robots. To create a robot, simply implements ",(0,a.kt)("a",{parentName:"p",href:"./reference/fido/robot/robot"},(0,a.kt)("inlineCode",{parentName:"a"},"Robot")),". For a robot to be ROS compatible, it should also implements ",(0,a.kt)("a",{parentName:"p",href:"./reference/fido/ros/protocol#robotprotocol-objects"},(0,a.kt)("inlineCode",{parentName:"a"},"RobotProtocol")),"."),(0,a.kt)("p",null,"See ",(0,a.kt)("a",{parentName:"p",href:"./reference/fido/robot/turtlebot3"},(0,a.kt)("inlineCode",{parentName:"a"},"Turtlebot3"))," for an example implementation."))}d.isMDXComponent=!0}}]);