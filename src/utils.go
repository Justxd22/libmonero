/*
 * This file is part of OpenMonero's Go library monero.go
 *
 * Copyright (c) 2023 OpenMonero
 * All Rights Reserved.
 * The code is distributed under MIT license, see LICENSE file for details.
 * Generated by OpenMonero on 03-07-2023.
 *
 */

package monero

import "regexp"

func Version() string {
	return "0.1.1"
}

func ValidateAddress(address string) bool {
	match, _ := regexp.MatchString(`^4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$`, address)
	return match
}
