const EduToken = artifacts.require("EduToken");

contract("EduToken", accounts => {
  let token;

  before(async () => {
    token = await EduToken.deployed();
  });

  it("should deploy EduToken contract", async () => {
    assert(token.address !== "");
  });

  it("should mint the correct initial supply", async () => {
    const balance = await token.balanceOf(accounts[0]);
    assert.equal(balance.toString(), web3.utils.toWei('1000000', 'ether'));
  });
});
