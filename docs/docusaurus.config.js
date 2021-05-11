/** @type {import('@docusaurus/types').DocusaurusConfig} */
module.exports = {
  title: "Fido",
  tagline: "End-to-end platform for robot development",
  url: "https://hojulian.github.io",
  baseUrl: "/fido/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon:
    "data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🔮</text></svg>",
  organizationName: "hojulian",
  projectName: "fido",
  themeConfig: {
    navbar: {
      title: "Fido",
      logo: {
        alt: "Fido",
        src: "data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🔮</text></svg>",
      },
      items: [
        {
          type: "doc",
          docId: "intro",
          position: "left",
          label: "Docs",
        },
        {
          type: "doc",
          docId: "reference/api",
          label: "API",
          position: "left",
        },
        {
          href: "https://github.com/hojulian/fido",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Fido",
          items: [
            {
              label: "Docs",
              to: "/docs/intro",
            },
            {
              label: "API",
              to: "/docs/reference/api",
            },
          ],
        },
        {
          title: "More",
          items: [
            {
              label: "GitHub",
              href: "https://github.com/hojulian/fido",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Julian Ho. Built with Docusaurus.`,
    },
    prism: {
      defaultLanguage: "python",
      theme: require("prism-react-renderer/themes/vsLight"),
      darkTheme: require("prism-react-renderer/themes/vsDark"),
    },
  },
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          editUrl: "https://github.com/hojulian/fido/edit/documentation/docs/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
};
