/* Keep diagram colours and fonts in sync with the site's light/dark profile. */
document.addEventListener("DOMContentLoaded", () => {
  const diagrams = [...document.querySelectorAll(".mermaid")];
  if (!diagrams.length) return;

  const sources = diagrams.map((diagram) => diagram.textContent);
  let dark = document.documentElement.classList.contains("dark");
  let pending = Promise.resolve();

  function render() {
    // Mermaid has global configuration: serialize renders when the theme changes.
    pending = pending.then(async () => {
      await document.fonts.ready;
      const isDark = document.documentElement.classList.contains("dark");
      const text = isDark ? "#f3f4f6" : "#17181b";
      const surface = isDark ? "#28292d" : "#f4f4f4";
      const background = isDark ? "#17181b" : "#ffffff";
      const accent = isDark ? "#fe91b8" : "#550029";
      const muted = isDark ? "#b5b5bb" : "#5b5c62";
      const secondary = isDark ? "#40353b" : "#e4dfde";

      mermaid.initialize({
        startOnLoad: false,
        theme: "base",
        fontFamily: '"Bureau Sans", sans-serif',
        themeVariables: {
          darkMode: isDark,
          fontFamily: '"Bureau Sans", sans-serif',
          background,
          primaryColor: surface,
          primaryTextColor: text,
          primaryBorderColor: accent,
          secondaryColor: secondary,
          secondaryTextColor: text,
          secondaryBorderColor: muted,
          tertiaryColor: background,
          tertiaryTextColor: text,
          tertiaryBorderColor: muted,
          lineColor: muted,
          textColor: text,
          mainBkg: surface,
          nodeBorder: accent,
          clusterBkg: background,
          clusterBorder: muted,
          edgeLabelBackground: background,
          titleColor: text,
          actorBkg: surface,
          actorBorder: accent,
          actorTextColor: text,
          actorLineColor: muted,
          signalColor: text,
          signalTextColor: text,
          labelBoxBkgColor: surface,
          labelBoxBorderColor: muted,
          labelTextColor: text,
          loopTextColor: text,
          noteBkgColor: secondary,
          noteBorderColor: muted,
          noteTextColor: text,
          activationBkgColor: secondary,
          activationBorderColor: accent,
          sequenceNumberColor: background,
        },
      });

      diagrams.forEach((diagram, index) => {
        diagram.textContent = sources[index];
        diagram.removeAttribute("data-processed");
      });
      await mermaid.run({ nodes: diagrams });
    }).catch((error) => console.error("Could not render Mermaid diagrams", error));
  }

  render();
  new MutationObserver(() => {
    const nextDark = document.documentElement.classList.contains("dark");
    if (nextDark !== dark) {
      dark = nextDark;
      render();
    }
  }).observe(document.documentElement, { attributes: true, attributeFilter: ["class"] });
});
