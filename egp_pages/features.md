---
layout: egp
permalink: /features/
title: Features
description: "EGP's physics, networking, native extension and build systems, with links to current API and support contracts."
---
<div class="egp-page" markdown="1">

# Familiar workflows, focused integrations

EGP retains Godot's editor, scene system, rendering and scripting foundations.
The fork replaces selected systems and adds native development tools.

| System | EGP integration | Guide |
| --- | --- | --- |
| 2D physics | Box2D is the sole native backend behind PhysicsServer2D and ordinary physics nodes. | [Box2D]({{ site.docs_url }}/egp/box2d.html) |
| 3D physics | Box3D is the sole native backend; explicit worlds provide stable IDs, ordered commands, trusted local snapshots and network entity-to-body mapping. | [Box3D worlds]({{ site.docs_url }}/egp/explicit_world.html) |
| Networking | Yojimbo supplies encrypted admission, raw channels and bounded server-authoritative replication. | [Networking]({{ site.docs_url }}/egp/networking.html) |
| Language helpers | GDScript, C# and C++ facades share validated message and state encoding, ownership, interest and scene factories, with public declarations and three-language usage examples. | [Helper API]({{ site.docs_url }}/egp/helper_reference.html) |
| Prediction | Game-provided capture/restore/simulate callbacks support bounded local history, correction and replay. | [Prediction]({{ site.docs_url }}/egp/prediction.html) |
| C++ extensions | Editor scaffolding, CMake builds, source diagnostics, embedded SDK and export library publication. | [C++ tools]({{ site.docs_url }}/egp/cpp_extensions.html) |
| Runtime reload | Opted-in editor-run C#/C++ reload with compatible state retention and explicit repair/restart paths. | [Hot reload]({{ site.docs_url }}/egp/hot_reload.html) |
| FASTBuild | Local or distributed Windows x64 MSVC compilation, with SCons owning generation and linking. | [Builds]({{ site.docs_url }}/egp/fastbuild.html) |
| Network lab | Bounded dedicated/listen-host fixtures cover reconnect, impairment and server recovery, with opt-in local Box3D checkpoint restoration, replay and stable body mapping. | [Network lab]({{ site.docs_url }}/egp/network_lab.html) |

## Compatibility and support

Godot's scene multiplayer/RPC APIs and the Godot/Jolt native physics backends
are removed. Existing projects should follow the [migration guide]({{ site.docs_url }}/egp/migration.html).

Windows x64 is the initial qualification platform. Broad scene parity, other
platforms, scale, soak and performance require their own runtime evidence.
Production account authentication, token delivery and persistence belong to the
game/backend. Consult [support and qualification]({{ site.docs_url }}/egp/qualification.html)
for the documented scope.

Windows C#/C++ fixtures also cover repeated local session recovery and trusted
Box3D checkpoint restoration. The editor and relocated Debug/Release runs each
pass 133 interoperability assertions, including explicit same-process client
reset/rejoin with fresh admission and restored physics replication. See
[language testing]({{ site.docs_url }}/egp/language_testing.html) for the exact
scope; automatic recovery, independent-process server stalls and hot reload
during faults still require separate qualification.

</div>
