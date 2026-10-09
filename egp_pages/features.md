---
layout: egp
permalink: /features/
title: Features
description: "EGP's native Superpos integration, physics and development tools."
---
<div class="egp-page" markdown="1">

# Familiar workflows, native integrations

EGP retains Godot's editor, scene system and scripting foundations.

| System | EGP integration | Guide |
| --- | --- | --- |
| Rendering | Forward+ through Vulkan, Direct3D 12 or Metal; dummy backend for headless tools. | [Rendering]({{ site.docs_url }}/tutorials/rendering/renderers.html) |
| 2D physics | Native Box2D behind ordinary scene APIs. | [Box2D]({{ site.docs_url }}/egp/box2d.html) |
| 3D physics | Native Box3D and independent fixed-tick worlds with local snapshots. | [Box3D]({{ site.docs_url }}/egp/box3d.html) |
| Networking | Native Superpos core, explicit schemas, canonical objects, checked ownership, explicit scene projection and bounded authenticated packet delivery. | [Superpos]({{ site.docs_url }}/egp/networking_reference.html) |
| Language API | GDScript and matching generated C#/C++ bindings call the same native ClassDB implementation. | [Language API]({{ site.docs_url }}/egp/helper_reference.html) |
| Prediction | Registered native simulation providers and bounded history; solver adapters and portable recovery require qualification. | [Prediction]({{ site.docs_url }}/egp/prediction.html) |
| C++ tools | Editor scaffolding, native builds, diagnostics and matching embedded SDK. | [C++ tools]({{ site.docs_url }}/egp/cpp_extensions.html) |
| Reload | Opt-in editor-run C#/C++ reload; matching APIs and lifecycle contracts required. | [Reload]({{ site.docs_url }}/egp/hot_reload.html) |
| Builds | Native xmake generation, compilation and linking; matching managed assemblies use .NET/MSBuild. | [Builds]({{ site.docs_url }}/egp/xmake.html) |

## Networking migration

Superpos replaces the former transport and Superposition layer. Old helper
facades, connect tokens, RPC/spawner components and networking physics adapters
are incompatible. Native explicit capture and sequential projection use
`SuperposReplicator`; automatic scene spawning and the previous arena's gameplay
results require separate migration. Read the
[migration guide]({{ site.docs_url }}/egp/superpos_migration.html).

## Application examples

The physics showcase projects authenticated canonical poses between two
associations in one process. The remote courier arena exercises 100 bot
streams plus one playable client over UDP/DTLS, with per-stream network
impairments and blackout recovery. These are bounded application workloads;
they do not establish production capacity or automatic solver rollback. See
the [fixtures and demo guide]({{ site.docs_url }}/egp/network_lab.html) for
commands, recorded evidence and limits.

## Platform and qualification

Web exports are unsupported. visionOS supports Window rendering and an opt-in
experimental immersive Forward+ path. Physical Vision Pro rendering, tracking,
performance and lifecycle remain unqualified. Read the
[experimental guide]({{ site.docs_url }}/egp/visionos_experimental.html).

The separate adapter has isolated API, lifecycle, UDP and language-binding
fixtures. Current full-engine, template, SDK, solver and WAN/gameplay evidence
must be checked separately. See [support and qualification]({{ site.docs_url }}/egp/qualification.html).

</div>
