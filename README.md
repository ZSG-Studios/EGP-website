# EGP website

The project website for [EGP](https://github.com/ZSG-Studios/EGP-Engine), maintained by
ZSG-Studios and forked from [Godot's website](https://github.com/godotengine/godot-website).
It uses the upstream Jekyll/Sass styles, Montserrat assets and layout conventions.
The active pages describe EGP's implemented systems and link to the matching
[documentation fork](https://github.com/ZSG-Studios/EGP-docs).

## Build

The maintained EGP workspace temporarily requires all build stages to run on
the remote build PC. Run Jekyll there and reuse the canonical `_site` output.
Local source editing and checks that do not build remain permitted.

Install Ruby 4.0 and Bundler, then run:

```sh
bundle install
bundle exec jekyll build --config _config.yml,_config.egp.yml --strict_front_matter
python tools/check_site.py
```

For local preview without the GitHub Pages prefix:

```sh
bundle exec jekyll serve --config _config.yml,_config.egp.yml,_config.development.yml
```

## Edit

- `egp_pages/` contains all public EGP pages.
- `_layouts/egp.html` contains the EGP navigation, metadata and footer.
- `assets/css/egp.css` extends the upstream styles; the original fonts and main/header/footer CSS remain shared.
- `_config.egp.yml` selects the active site, documentation URL and deployment prefix.
- `tools/check_site.py` validates the built pages, local links, assets and attribution routing.

Upstream editorial, release, download and localization sources remain available
for merges but are excluded from the EGP build. Godot's service integrations and
download generators are not loaded. EGP does not claim Godot releases, donations,
community services or showcase projects as its own.

The build workflow retains the checked HTML artifact. The manually triggered
publish workflow deploys it to GitHub Pages. For a custom domain, update `url`,
`baseurl` and the linked documentation URL consistently, then rerun link checks.

Keep an `upstream` remote for `https://github.com/godotengine/godot-website.git`.
Merge upstream improvements explicitly and review changed styles/configuration.

## License

The upstream [MIT license](LICENSE.txt) and attribution to Godot Engine
contributors are retained. EGP is an independent ZSG-Studios fork.
