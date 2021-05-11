/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */

configuredSidebar = (sidebar) => {
  sidebar.collapsed = false;

  return sidebar;
};

module.exports = {
  mainSidebar: [
    {
      type: "doc",
      id: "intro",
      label: "Introduction",
    },
    {
      type: "doc",
      id: "getting-started",
      label: "Getting Started",
    },
    {
      type: "doc",
      id: "examples",
      label: "Examples",
    },
    {
      type: "doc",
      id: "concepts",
      label: "Concepts",
    },
    {
      type: "doc",
      id: "advanced",
      label: "Advanced Features",
    },
    {
      type: "doc",
      id: "contributing",
      label: "Contributing to Fido",
    },
    {
      type: "doc",
      id: "roadmap",
      label: "Roadmap",
    },
  ],

  apiSidebar: [
    {
      type: "doc",
      id: "reference/api",
      label: "Using API",
    },
    configuredSidebar(require("./docs/reference/sidebar.json")),
  ],
};
