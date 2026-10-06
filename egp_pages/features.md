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
pass 197 interoperability assertions and 27 validator steps. Recovery fixtures
include connected high-/low-level client reset/rejoin and independent high-level
server/client processes with native disconnect detection, fresh admission and
restored physics replication. Low-level checks cover retired handles and exact
raw payload delivery. See
[language testing]({{ site.docs_url }}/egp/language_testing.html) for the exact
scope; independent-process low-level faults, production admission/backoff and
recovery policy, hard outages and in-flight/concurrent reload still require separate
qualification.

An opt-in Windows Debug [network/reload test]({{ site.docs_url }}/egp/hot_reload.html#native-sessions-after-a-clock-fault)
also preserves native sessions across C++/C# reload after both sessions stop,
then verifies explicit fresh-token recovery. A separate [live reload gate]({{ site.docs_url }}/egp/hot_reload.html#live-sessions-during-reload)
keeps an authenticated pair connected across failed builds and C#/C++ reload,
with both outbound simulators configured for 30 ms latency, 5 ms jitter and
5 percent loss. This is local fixture evidence; actual packet drops, WAN behavior,
in-flight/concurrent reload, managed facade/event closure persistence and
exported-runtime reload require separate qualification.

The optional [physics reload gate]({{ site.docs_url }}/egp/hot_reload.html#native-physics-state-during-reload)
also retains one explicit Box3D world and stable body through live C#/C++ reload.
After a clock fault, it preserves the stopped world, rejects damaged snapshots
without changing state and explicitly restores a trusted local checkpoint before
fresh admission resumes physics. GDScript drives the fixture clock and baseline
codec; C++ and C# verify the same native body state. This covers one local Windows
Debug pair and one body. Automatic client rollback, larger worlds and production
checkpoint policy require separate qualification.

The public C# low-level session API now supports [explicit reload handoff]({{ site.docs_url }}/egp/hot_reload.html#c-session-ownership-and-events)
through `DetachForReload()` and `ResumeAfterReload(Dictionary)`. Applications
transfer a local capsule in serialization hooks and resubscribe their event
handlers. Live and stopped reload fixtures verify ownership, invalid/copied
claims and constant native signal connection counts. Fresh editor/Debug/Release
language runs validate the updated helpers. This capsule transfers low-level
ownership; high-level C++/physics adapter ownership and
arbitrary captured closures require separate qualification.

High-level C# [NetNode reload]({{ site.docs_url }}/egp/hot_reload.html#high-level-c-node-reload)
now preserves forwarding on the same codec child during serialization. Owners
resubscribe ordinary application events, use named Godot message handlers and
call base from derived serialization overrides. Live/stopped fixtures verify
messages, owned inputs, raw packets and all eleven forwarding connections.
Tree exit/reentry and freed codec replacement are checked; traffic after reentry
and assembly/unload/ABI failures during authenticated node traffic remain open.

</div>
