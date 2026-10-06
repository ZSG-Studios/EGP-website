---
layout: egp
permalink: /community/
title: Contribute
description: "Contribute to EGP's engine, documentation and website, or report reproducible fork-specific issues."
---
<div class="egp-page" markdown="1">

# Contribute to EGP

EGP is maintained by ZSG-Studios. Contributions should describe the concrete
problem, the resulting behavior and the validation performed.

## Report an issue

Use the [EGP issue tracker]({{ site.engine_url }}/issues) for engine problems.
Include a minimal reproduction, source revision, platform, editor/template
identity and relevant logs. Keep admission tokens and private keys out of reports.

Report manual problems in [EGP-docs](https://github.com/ZSG-Studios/EGP-docs/issues)
and website problems in [EGP-website](https://github.com/ZSG-Studios/EGP-website/issues).

## Improve the documentation

Native API descriptions live in the engine's XML class reference. System guides
live in the engine's `doc/` directory and networking module. The documentation
fork owns its tutorials, migration pages and presentation. Use the
[synchronization workflow]({{ site.docs_url }}/egp/documentation.html) to regenerate
the published reference and record its source hashes.

## Work with upstream

The engine, manual and website retain their Godot upstream history. Keep EGP
changes focused so upstream improvements can be merged and reviewed. Fork-specific
changes belong in the EGP repositories; Godot's project services remain operated
by the Godot community.

</div>
