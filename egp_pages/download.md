---
layout: egp
permalink: /download/
title: Build & download
description: "Build EGP from source and select matching editor, export templates, C# assemblies and C++ SDK."
---
<div class="egp-page" markdown="1">

# Build EGP

Start with the [engine source]({{ site.engine_url }}). Use the editor and export
templates from the same EGP revision, including matching C# assemblies and the
editor's generated C++ SDK.

## Windows

Install Visual Studio's C++ desktop workload, the Windows SDK and the .NET SDK.
Run from PowerShell:

```powershell
git clone --recurse-submodules https://github.com/ZSG-Studios/EGP.git
cd EGP
.\misc\scripts\build_egp.ps1 -Setup
.\misc\scripts\build_egp.ps1 -Local -Target editor
.\misc\scripts\build_egp.ps1 -Local -Target template_debug
.\misc\scripts\build_egp.ps1 -Local -Target template_release
```

The launcher embeds the editor's actual extension API and builds managed
assemblies. Distributed compilation is available with a configured FASTBuild
worker; read the [FASTBuild guide]({{ site.docs_url }}/egp/fastbuild.html).

## Published artifacts

Check [EGP releases]({{ site.engine_url }}/releases) and successful
[engine CI runs]({{ site.engine_url }}/actions) for available artifacts and their
matching source revision. Availability depends on the build. Official Godot
downloads do not include EGP's replacements.

## Other desktop platforms

Use the inherited Godot compilation workflow and EGP's exact-API editor build
script. Confirm the intended platform and feature set against the
[qualification record]({{ site.docs_url }}/egp/qualification.html).

Physics currently requires a single-precision x86_64 or arm64 desktop build.
Android, iOS, Web and double-precision exports omit physics explicitly; games
requiring physics need a supported desktop build. Android and double-precision
editors are currently unsupported.

## Make a game

Read [getting started]({{ site.docs_url }}/egp/getting_started.html), install
the [networking helpers]({{ site.docs_url }}/egp/networking.html) if needed,
and use the [C++ editor tools]({{ site.docs_url }}/egp/cpp_extensions.html)
for native extensions. Import existing projects into a separate working copy
and follow the [migration guide]({{ site.docs_url }}/egp/migration.html).

</div>
