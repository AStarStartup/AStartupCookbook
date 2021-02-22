/* Astartup Cookbook @version 0.x
@link    github.com/kabuki-starship/astartup.cookbook.git
@file    /_seams/release.h
@author  Cale McCollough <https://cale-mccollough.github.io>
@license Copyright 2014-9 (C) Cale McCollough; all rights reserved (R). This
source code form is covered under the Kabuki Strong Source-available License.
A copy of the license that YOU MUST READ can be found in the readme.md file
in this folder. */

#pragma once
#include <_config.h>

#if SEAM == ASTARTUP_COOKBOOK_RELEASE
#include "_debug.inl"
#else
#include "_release.inl"
#endif

using namespace _;

namespace astartup {
namespace cookbook {
inline const CHA* Release(CHA* seam_log, CHA* seam_end, const CHA* args) {
#if SEAM >= ASTARTUP_COOKBOOK_RELEASE
  TEST_BEGIN;

  PRINT_HEADING("Testing Foo fun.");

#endif
  return 0;
}
}  // namespace cookbook
}  // namespace astartup
