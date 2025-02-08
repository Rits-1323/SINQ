const EduToken = artifacts.require("EduToken");
const EduCertificate = artifacts.require("EduCertificate");
const Scholarship = artifacts.require("Scholarship");


module.exports = async function (deployer) {
  const initialSupply = web3.utils.toWei("1000000", "ether"); // 1 million ETK

  await deployer.deploy(EduToken, initialSupply);



  // Deploy EduCertificate contract
  await deployer.deploy(EduCertificate);

  // Deploy Scholarship contract
  await deployer.deploy(Scholarship);
};
