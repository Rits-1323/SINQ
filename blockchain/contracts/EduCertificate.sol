library Counters {
    struct Counter {
        uint256 _value;
    }

    function current(Counter storage counter) internal view returns (uint256) {
        return counter._value;
    }

    function increment(Counter storage counter) internal {
        unchecked {
            counter._value += 1;
        }
    }

    function reset(Counter storage counter) internal {
        counter._value = 0;
    }
}

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract EduCertificate is ERC721 {
    using Counters for Counters.Counter;

    struct Counter {
        uint256 _value;
    }
    Counter private _tokenIdCounter;

    constructor() ERC721("EduCertificate", "ECERT") {}

    function safeMint(address to) public returns (uint256) {
        _tokenIdCounter._value += 1;
        uint256 tokenId = _tokenIdCounter._value;
        _safeMint(to, tokenId);
        return tokenId;
    }
}
