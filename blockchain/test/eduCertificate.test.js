const EduCertificate = artifacts.require("EduCertificate");

contract("EduCertificate", accounts => {
  let certificate;

  before(async () => {
    certificate = await EduCertificate.deployed();
  });

  it("should mint an EduCertificate", async () => {
    const receipt = await certificate.safeMint(accounts[0]);
    assert.equal(receipt.logs[0].event, "Transfer");
  });
});
