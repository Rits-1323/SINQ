// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Scholarship {
    address public admin;
    mapping(address => uint256) public scholarshipBalance;

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can execute this");
        _;
    }

    constructor() {
        admin = msg.sender;
    }

    function fundScholarship(
        address student,
        uint256 amount
    ) external onlyAdmin {
        scholarshipBalance[student] += amount;
    }

    function withdrawScholarship(uint256 amount) external {
        require(
            scholarshipBalance[msg.sender] >= amount,
            "Insufficient balance"
        );
        scholarshipBalance[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to receive funds
    receive() external payable {}
}
