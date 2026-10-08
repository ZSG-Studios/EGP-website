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
| Superposition | Inspector session setup, allowlisted scene spawning, selected property replication, acknowledged deltas and typed RPC with authenticated ownership, relevance and update budgets. | [Superposition]({{ site.docs_url }}/egp/superposition.html) |
| Motion presentation | Native buffered snapshot interpolation separates rendered poses from authoritative fixed-step physics. | [Physics arena]({{ site.docs_url }}/egp/physics_arena.html) |
| Language helpers | GDScript, C# and C++ facades share validated message and state encoding, ownership, interest and scene factories, with public declarations and three-language usage examples. | [Helper API]({{ site.docs_url }}/egp/helper_reference.html) |
| Prediction | Native complete-world canonical-input reconciliation and an Inspector Box3D adapter support bounded local history, hash verification and replay; games supply matching genesis and authorized complete inputs. | [Prediction]({{ site.docs_url }}/egp/prediction.html) |
| C++ extensions | Editor scaffolding, native xmake builds, source diagnostics, embedded SDK and export library publication. | [C++ tools]({{ site.docs_url }}/egp/cpp_extensions.html) |
| Runtime reload | Opted-in editor-run C#/C++ reload with compatible state retention and explicit repair/restart paths. | [Hot reload]({{ site.docs_url }}/egp/hot_reload.html) |
| Native builds | Lua generation and native xmake compilation, linking, exact-API SDK packaging and isolated variant caches. | [Builds]({{ site.docs_url }}/egp/xmake.html) |
| Network lab | Bounded dedicated/listen-host fixtures cover reconnect, impairment and server recovery, with opt-in local Box3D checkpoint restoration, replay and stable body mapping. | [Network lab]({{ site.docs_url }}/egp/network_lab.html) |

## Compatibility and support

The published source includes official Godot changes through
[`e7b12e7492`](https://github.com/godotengine/godot/commit/e7b12e749220a75ef87e800e080bd2732ad46854).
The Windows regression gate repeats language, physics, reload, networking and
admission checks. Inherited GDScript/C# scene references now survive unmodified
binary export, with 108 reference assertions across editor and relocated
Debug/Release games. Separate checks retain export-plugin changes. Read the
[source and artifact qualification]({{ site.docs_url }}/egp/qualification.html#published-upstream-consolidation)
for the compiled revisions, zstd guard validation and remaining coverage.

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
ownership. C++ has a separate explicit handoff contract below; arbitrary captured
closures require separate qualification.

High-level C# [NetNode reload]({{ site.docs_url }}/egp/hot_reload.html#high-level-c-node-reload)
now preserves forwarding on the same codec child during serialization. Owners
resubscribe ordinary application events, use named Godot message handlers and
call base from derived serialization overrides. Live/stopped fixtures verify
messages, owned inputs, raw packets and all eleven forwarding connections.
Tree exit/reentry and freed codec replacement are checked. Current fixtures each
verify three fresh-session traffic cycles after reentry. Assembly/unload/ABI
failures during authenticated node traffic remain open.

The shared [codec lifetime contract]({{ site.docs_url }}/egp/hot_reload.html#native-session-lifetime-and-reentry)
retains callbacks/session on Stop and disconnects all seven native callbacks on
Close. Fresh-session tests verify retired callback isolation, exact ownership
traffic and specific close/stop state-callback replacements. Reconfigure custom
options before new host/join, and keep saved handles tied to their issuing native
session; numeric IDs can repeat in a new session. Local stale-signal injection is
a lifetime test; remote-attack and WAN behavior require separate qualification.
Arbitrary in-flight mutation and performance remain open.

The public C# [Box3D adapter reload API]({{ site.docs_url }}/egp/hot_reload.html#c-box3d-adapter-ownership)
transfers the existing adapter, world and stable body mapping through a local
capsule. Applications resubscribe events after resume. Fresh live/stopped fixtures
verify exact callback counts, 22 ownership checks each, tree reentry and three
fresh-session cycles with resumed client physics. Commands defer until the active
poll/tick returns; arbitrary callback mutation remains unqualified. Fresh
editor/Debug/Release language builds and low-level/default runtime regressions
pass. Automatic C++ ownership transfer, authenticated-node repair failures and
concurrent/exported-runtime reload remain open.

C++ [network and Box3D ownership handoff]({{ site.docs_url }}/egp/hot_reload.html#c-network-and-box3d-ownership)
uses `detach_for_reload()` and `resume_after_reload()` with local, single-use
capsules stored in extension-node properties. Applications pause manual polling
at a safe boundary, transfer their owners and resubscribe callbacks after reload.
Two actual compatible Debug DLL reloads retain native sessions, adapter/world
identities and body mapping, with 60 capsule checks and 138 runtime assertions.
Fresh editor/Debug/Release language regressions also pass. A separate short
missing/invalid-DLL recovery fixture passes four failed loads and two compatible
repairs with 158 runtime assertions; observed fault intervals were 25 ms and
14 ms with polling paused. Automatic/in-flight transfer, prolonged faults and
exported-game reload require separate qualification.

</div>
